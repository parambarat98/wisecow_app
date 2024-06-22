# -*- coding: utf-8 -*- #
# Copyright 2021 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Common utilities to operate with Docker."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import collections
import datetime
import re
from googlecloudsdk.command_lib.ai import errors
from googlecloudsdk.command_lib.ai.custom_jobs import local_util
from googlecloudsdk.core import log

_MAX_REPOSITORY_LENGTH = 255
_MAX_TAG_LENGTH = 128

_AUTONAME_PREFIX = "cloudai-autogenerated"
_DEFAULT_IMAGE_NAME = "unnamed"
_DEFAULT_REPO_REGION = "us"

Package = collections.namedtuple("Package",
                                 ["script", "package_path", "python_module"])
Image = collections.namedtuple("Image",
                               ["name", "default_home", "default_workdir"])


def _ParseRepositoryTag(image_name):
  """Parses out the repository and tag from a Docker image name.

  Args:
    image_name: (str) The full name of an image, expected to be in a format of
      "repository[:tag]"

  Returns:
    A (repository, tag) tuple representing the parsed result.
    None repository means the image name is invalid; tag may be None if it isn't
    present in the given image name.
  """

  if image_name.count(":") > 2:
    return None, None

  parts = image_name.rsplit(":", 1)
  if len(parts) == 2 and "/" not in parts[1]:
    return tuple(parts)

  return image_name, None


def _ParseRepositoryHost(repository_name):
  """Parses a repository to an optional hostname and a list of path compoentes.

  Args:
    repository_name: (str) A name made up of slash-separated path name
      components, optionally prefixed by a registry hostname.

  Returns:
    A (hostname, components) tuple representing the parsed result.
    The hostname will be None if it isn't present; the components is a list of
    each slash-separated part in the given repository name.
  """

  components = repository_name.split("/")

  if len(components) == 1:
    return None, components

  if "." in components[0] or ":" in components[0]:
    # components[0] is regarded as a hostname
    return components[0], components[1:]

  return None, components


def _ParseHostPort(host):
  """Parses a registry hostname to a list of components and an optional port.

  Args:
    host: (str) The registry hostname supposed to comply with standard DNS
      rules, optionally be followed by a port number in the format like ":8080".

  Returns:
    A (hostcomponents, port) tuple representing the parsed result.
    The hostcomponents contains each dot-seperated component in the given
    hostname; port may be None if it isn't present.
  """

  parts = host.rsplit(":", 1)
  hostcomponents = parts[0].split(".")
  port = parts[1] if len(parts) == 2 else None

  return hostcomponents, port


def ValidateRepositoryAndTag(image_name):
  r"""Validate the given image name is a valid repository/tag reference.

  As explained in
  https://docs.docker.com/engine/reference/commandline/tag/#extended-description,
  a valid repository/tag reference should following the below pattern:

  reference             := name [ ":" tag ]
  name                  := [hostname '/'] component ['/' component]*
  hostname              := hostcomponent ['.' hostcomponent]* [':' port-number]
  hostcomponent         := /([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9])/
  port-number           := /[0-9]+/
  component             := alpha-numeric [separator alpha-numeric]*
  alpha-numeric         := /[a-z0-9]+/
  separator             := /[_.]|__|[-]*/

  tag                   := /[\w][\w.-]{0,127}/

  Args:
    image_name: (str) Full name of a Docker image.

  Raises:
    ValueError if the image name is not valid.
  """
  repository, tag = _ParseRepositoryTag(image_name)

  if repository is None:
    raise ValueError("Unable to parse repository and tag.")

  if len(repository) > _MAX_REPOSITORY_LENGTH:
    raise ValueError(
        "Repository name must not be more than {} characters.".format(
            _MAX_REPOSITORY_LENGTH))

  hostname, path_components = _ParseRepositoryHost(repository)

  if hostname:
    hostcomponents, port = _ParseHostPort(hostname)

    hostcomponent_regex = r"^(?:[a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9])$"
    for hostcomponent in hostcomponents:
      if re.match(hostcomponent_regex, hostcomponent) is None:
        raise ValueError(
            "Invalid hostname/port \"{}\" in repository name.".format(hostname))

    port_regex = r"^[0-9]+$"
    if port and re.match(port_regex, port) is None:
      raise ValueError(
          "Invalid hostname/port \"{}\" in repository name.".format(hostname))

  for component in path_components:
    if not component:
      raise ValueError("Empty path component in repository name.")

    component_regex = r"^[a-z0-9]+(?:(?:[._]|__|[-]*)[a-z0-9]+)*$"
    if re.match(component_regex, component) is None:
      raise ValueError(
          "Invalid path component \"{}\" in repository name.".format(component))

  if tag:
    if len(tag) > _MAX_TAG_LENGTH:
      raise ValueError("Tag name must not be more than {} characters.".format(
          _MAX_TAG_LENGTH))

    tag_regex = r"^[\w][\w.-]{0,127}$"
    if re.match(tag_regex, tag) is None:
      raise ValueError("Invalid tag.")


def GenerateImageName(base_name=None, project=None, region=None, is_gcr=False):
  """Generate a name for the Docker image built by AI platform gcloud."""
  sanitized_name = _SanitizeRepositoryName(base_name or _DEFAULT_IMAGE_NAME)

  # Use the current timestamp as the tag.
  tag = datetime.datetime.now().strftime("%Y%m%d.%H.%M.%S.%f")
  image_name = "{}/{}:{}".format(_AUTONAME_PREFIX, sanitized_name, tag)

  if project:
    if is_gcr:
      repository = "gcr.io"
    else:
      region_prefix = region or _DEFAULT_REPO_REGION
      repository = "{}-docker.pkg.dev".format(region_prefix)
    return "{}/{}/{}".format(repository, project.replace(":", "/"), image_name)
  return image_name


def _SanitizeRepositoryName(name):
  """Sanitizes the given name to make it valid as an image repository.

  As explained in
  https://docs.docker.com/engine/reference/commandline/tag/#extended-description,
  Valid name may contain only lowercase letters, digits and separators.
  A separator is defined as a period, one or two underscores, or one or more
  dashes. A name component may not start or end with a separator.

  This method will replace the illegal characters in the given name and strip
  starting and ending separator characters.

  Args:
    name: str, the name to sanitize.

  Returns:
    A sanitized name.
  """
  return re.sub("[._][._]+|[^a-z0-9._-]+", ".", name.lower()).strip("._-")


def ExecuteDockerCommand(command):
  """Executes Docker CLI commands in subprocess.

  Just calls local_util.ExecuteCommand(cmd,...) and raises error for non-zero
  exit code.

  Args:
    command: (List[str]) Strings to send in as the command.

  Raises:
    ValueError: The input command is not a docker command.
    DockerError: An error occurred when executing the given docker command.
  """

  command_str = " ".join(command)
  if not command_str.startswith("docker"):
    raise ValueError("`{}` is not a Docker command".format("docker"))

  log.info("Running command: {}".format(command_str))

  return_code = local_util.ExecuteCommand(command)
  if return_code != 0:
    error_msg = """
        Docker failed with error code {code}.
        Command: {cmd}
        """.format(
            code=return_code, cmd=command_str)
    raise errors.DockerError(error_msg, command, return_code)

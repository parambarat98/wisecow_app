"""Generated client library for policyanalyzer version v1."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.generated_clients.apis.policyanalyzer.v1 import policyanalyzer_v1_messages as messages


class PolicyanalyzerV1(base_api.BaseApiClient):
  """Generated client library for service policyanalyzer version v1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://policyanalyzer.googleapis.com/'
  MTLS_BASE_URL = 'https://policyanalyzer.mtls.googleapis.com/'

  _PACKAGE = 'policyanalyzer'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1'
  _CLIENT_ID = 'CLIENT_ID'
  _CLIENT_SECRET = 'CLIENT_SECRET'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'PolicyanalyzerV1'
  _URL_VERSION = 'v1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new policyanalyzer handle."""
    url = url or self.BASE_URL
    super(PolicyanalyzerV1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.folders_locations_activityTypes_activities = self.FoldersLocationsActivityTypesActivitiesService(self)
    self.folders_locations_activityTypes = self.FoldersLocationsActivityTypesService(self)
    self.folders_locations = self.FoldersLocationsService(self)
    self.folders = self.FoldersService(self)
    self.organizations_locations_activityTypes_activities = self.OrganizationsLocationsActivityTypesActivitiesService(self)
    self.organizations_locations_activityTypes = self.OrganizationsLocationsActivityTypesService(self)
    self.organizations_locations = self.OrganizationsLocationsService(self)
    self.organizations = self.OrganizationsService(self)
    self.projects_locations_activityTypes_activities = self.ProjectsLocationsActivityTypesActivitiesService(self)
    self.projects_locations_activityTypes = self.ProjectsLocationsActivityTypesService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)

  class FoldersLocationsActivityTypesActivitiesService(base_api.BaseApiService):
    """Service class for the folders_locations_activityTypes_activities resource."""

    _NAME = 'folders_locations_activityTypes_activities'

    def __init__(self, client):
      super(PolicyanalyzerV1.FoldersLocationsActivityTypesActivitiesService, self).__init__(client)
      self._upload_configs = {
          }

    def Query(self, request, global_params=None):
      r"""Queries policy activities on Google Cloud resources.

      Args:
        request: (PolicyanalyzerFoldersLocationsActivityTypesActivitiesQueryRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudPolicyanalyzerV1QueryActivityResponse) The response message.
      """
      config = self.GetMethodConfig('Query')
      return self._RunMethod(
          config, request, global_params=global_params)

    Query.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/folders/{foldersId}/locations/{locationsId}/activityTypes/{activityTypesId}/activities:query',
        http_method='GET',
        method_id='policyanalyzer.folders.locations.activityTypes.activities.query',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1/{+parent}/activities:query',
        request_field='',
        request_type_name='PolicyanalyzerFoldersLocationsActivityTypesActivitiesQueryRequest',
        response_type_name='GoogleCloudPolicyanalyzerV1QueryActivityResponse',
        supports_download=False,
    )

  class FoldersLocationsActivityTypesService(base_api.BaseApiService):
    """Service class for the folders_locations_activityTypes resource."""

    _NAME = 'folders_locations_activityTypes'

    def __init__(self, client):
      super(PolicyanalyzerV1.FoldersLocationsActivityTypesService, self).__init__(client)
      self._upload_configs = {
          }

  class FoldersLocationsService(base_api.BaseApiService):
    """Service class for the folders_locations resource."""

    _NAME = 'folders_locations'

    def __init__(self, client):
      super(PolicyanalyzerV1.FoldersLocationsService, self).__init__(client)
      self._upload_configs = {
          }

  class FoldersService(base_api.BaseApiService):
    """Service class for the folders resource."""

    _NAME = 'folders'

    def __init__(self, client):
      super(PolicyanalyzerV1.FoldersService, self).__init__(client)
      self._upload_configs = {
          }

  class OrganizationsLocationsActivityTypesActivitiesService(base_api.BaseApiService):
    """Service class for the organizations_locations_activityTypes_activities resource."""

    _NAME = 'organizations_locations_activityTypes_activities'

    def __init__(self, client):
      super(PolicyanalyzerV1.OrganizationsLocationsActivityTypesActivitiesService, self).__init__(client)
      self._upload_configs = {
          }

    def Query(self, request, global_params=None):
      r"""Queries policy activities on Google Cloud resources.

      Args:
        request: (PolicyanalyzerOrganizationsLocationsActivityTypesActivitiesQueryRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudPolicyanalyzerV1QueryActivityResponse) The response message.
      """
      config = self.GetMethodConfig('Query')
      return self._RunMethod(
          config, request, global_params=global_params)

    Query.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/organizations/{organizationsId}/locations/{locationsId}/activityTypes/{activityTypesId}/activities:query',
        http_method='GET',
        method_id='policyanalyzer.organizations.locations.activityTypes.activities.query',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1/{+parent}/activities:query',
        request_field='',
        request_type_name='PolicyanalyzerOrganizationsLocationsActivityTypesActivitiesQueryRequest',
        response_type_name='GoogleCloudPolicyanalyzerV1QueryActivityResponse',
        supports_download=False,
    )

  class OrganizationsLocationsActivityTypesService(base_api.BaseApiService):
    """Service class for the organizations_locations_activityTypes resource."""

    _NAME = 'organizations_locations_activityTypes'

    def __init__(self, client):
      super(PolicyanalyzerV1.OrganizationsLocationsActivityTypesService, self).__init__(client)
      self._upload_configs = {
          }

  class OrganizationsLocationsService(base_api.BaseApiService):
    """Service class for the organizations_locations resource."""

    _NAME = 'organizations_locations'

    def __init__(self, client):
      super(PolicyanalyzerV1.OrganizationsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

  class OrganizationsService(base_api.BaseApiService):
    """Service class for the organizations resource."""

    _NAME = 'organizations'

    def __init__(self, client):
      super(PolicyanalyzerV1.OrganizationsService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsLocationsActivityTypesActivitiesService(base_api.BaseApiService):
    """Service class for the projects_locations_activityTypes_activities resource."""

    _NAME = 'projects_locations_activityTypes_activities'

    def __init__(self, client):
      super(PolicyanalyzerV1.ProjectsLocationsActivityTypesActivitiesService, self).__init__(client)
      self._upload_configs = {
          }

    def Query(self, request, global_params=None):
      r"""Queries policy activities on Google Cloud resources.

      Args:
        request: (PolicyanalyzerProjectsLocationsActivityTypesActivitiesQueryRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudPolicyanalyzerV1QueryActivityResponse) The response message.
      """
      config = self.GetMethodConfig('Query')
      return self._RunMethod(
          config, request, global_params=global_params)

    Query.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/activityTypes/{activityTypesId}/activities:query',
        http_method='GET',
        method_id='policyanalyzer.projects.locations.activityTypes.activities.query',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1/{+parent}/activities:query',
        request_field='',
        request_type_name='PolicyanalyzerProjectsLocationsActivityTypesActivitiesQueryRequest',
        response_type_name='GoogleCloudPolicyanalyzerV1QueryActivityResponse',
        supports_download=False,
    )

  class ProjectsLocationsActivityTypesService(base_api.BaseApiService):
    """Service class for the projects_locations_activityTypes resource."""

    _NAME = 'projects_locations_activityTypes'

    def __init__(self, client):
      super(PolicyanalyzerV1.ProjectsLocationsActivityTypesService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = 'projects_locations'

    def __init__(self, client):
      super(PolicyanalyzerV1.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(PolicyanalyzerV1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }

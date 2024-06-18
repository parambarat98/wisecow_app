# Use an official Ubuntu as a parent image
FROM ubuntu:20.04

# Set the maintainer label
LABEL maintainer="yourname@example.com"

# Install required packages
RUN apt-get update && \
    apt-get install -y fortune cowsay netcat

# Set the working directory
WORKDIR /app

# Copy the wisecow.sh script into the container
COPY wisecow.sh /app/wisecow.sh

# Make the script executable
RUN chmod +x /app/wisecow.sh

# Expose the port that the app will run on
EXPOSE 4499

# Run the Wisecow application
CMD ["/app/wisecow.sh"]

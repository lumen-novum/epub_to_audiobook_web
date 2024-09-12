# Use an official Python runtime as a parent image
FROM python:3.11-slim-bookworm

# Set the source directory in the container
WORKDIR /app_src

# Add current directory code to docker
ADD . /app_src

# Install ffmpeg
RUN apt-get update && apt-get install -y ffmpeg

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set this as the default command
ENTRYPOINT [ "flask", "run", "--host=0.0.0.0"]
FROM debian:latest
# Use an official Python runtime as the base image
FROM python:3.9

# install packages
RUN apt update
RUN apt install -y python3

# copy script inside container
COPY docker-run.sh /root/

# Copy the requirements file into the container
COPY requirements.txt /root/

# Install the required dependencies
RUN pip install --no-cache-dir -r /root/requirements.txt 

# copy script inside container
COPY v1.py /root/

# copy script inside container
COPY v2.py /root/

# copy script inside container
COPY v4.py /root/

# copy script inside container
COPY v3.py /root/

# run when container starts
CMD ["bash", "/root/docker-run.sh"]

# pull official base image
FROM python:3.11

# Set working dir
WORKDIR app/

# set environment variables
# TODO Figure out purpose
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r  requirements.txt

# Copy project
COPY . /app/
# Pull base image
FROM python:3.11

# Set environmet variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work dir
WORKDIR /application

# Install dependencies
COPY Pipfile Pipfile.lock /application/
RUN pip install pipenv && pipenv install --system

# Copy project
COPY . /application/
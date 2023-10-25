FROM python:3.11

# Install system packages
RUN apt-get update && apt-get install -y curl

# Install pip for Python 3.11
RUN curl -sS https://bootstrap.pypa.io/get-pip.py | python3.11 -

# Upgrade pip for Python 3.11
RUN python3.11 -m pip install --upgrade pip

# Install Django and Django REST framework using pip for Python 3.11
RUN python3.11 -m pip install django djangorestframework

# Clean up
#RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Set the working directory for your application
#WORKDIR /app

# Add your application files to the container
# COPY . /app

# You can add more configuration or commands specific to your application here

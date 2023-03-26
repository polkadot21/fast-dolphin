# Use an official Python runtime as a parent image
FROM python:3.9

#By setting the PYTHONUNBUFFERED environment variable to 1, you're telling Python to disable this buffering behavior. This ensures that output is immediately flushed to the console or logs, so you can see what's happening in real-time.
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV PYTHONUNBUFFERED 1

# Set the working directory to /app
WORKDIR /app

ADD https://github.com/aws/aws-lambda-runtime-interface-emulator/releases/latest/download/aws-lambda-rie /opt/venv/bin/aws-lambda-rie
RUN chmod +x /opt/venv/bin/aws-lambda-rie
COPY entry.sh .

RUN python3 -m pip install awslambdaric

# Copy the requirements file into the container at /app
COPY requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy the rest of the app code into the container at /app
COPY . /app

ENTRYPOINT [ "sh", "entry.sh" ]
CMD [ "main.handler" ]
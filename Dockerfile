FROM python:3.8

RUN apt-get update && \
      apt-get install -y \
      build-essential default-libmysqlclient-dev

# Create app directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt ./

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

# Bundle app source
COPY . /app

EXPOSE 5000

ENV FLASK_ENV Production

ENV FLASK_DEBUG 0

# Run
CMD [ "make", "run_prod" ]
#/bin/bash

export AWS_ACCESS_KEY_ID=AKIAYA33NDMX6PQY3PL2
export AWS_SECRET_ACCESS_KEY=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
export AWS_DEFAULT_REGION=ap-southeast-1

APPNAME=myserver
REPOSITORY=551625235247.dkr.ecr.ap-southeast-1.amazonaws.com
VERSION=0.0.10

docker build -t ${APPNAME} nginx
docker tag ${APPNAME}:latest ${REPOSITORY}/${APPNAME}:${VERSION}

aws ecr get-login-password --region ap-southeast-1 | docker login --username AWS --password-stdin ${REPOSITORY}
docker push ${REPOSITORY}/${APPNAME}:${VERSION}
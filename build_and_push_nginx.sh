#/bin/bash

export AWS_ACCESS_KEY_ID=AKIAYA33NDMXZXJE5Q7I
export AWS_SECRET_ACCESS_KEY=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
export AWS_DEFAULT_REGION=ap-southeast-1

APPNAME=myserver
REPOSITORY=551625235247.dkr.ecr.ap-southeast-1.amazonaws.com
VERSION=0.0.3

docker build -t ${APPNAME} nginx
docker tag ${APPNAME}:latest ${REPOSITORY}/${APPNAME}:${VERSION}

aws ecr get-login-password --region ap-southeast-1 | docker login --username AWS --password-stdin ${REPOSITORY}
docker push ${REPOSITORY}/${APPNAME}:${VERSION}
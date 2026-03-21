#!/bin/bash

FILE_NAME=$1
BUCKET_NAME=$2
EXPIRATION_TIME_SECONDS=604800

aws s3 cp "$FILE_NAME" "s3://$BUCKET_NAME/"

BASENAME=$(basename "$FILE_NAME") #takes just the name part of the file so a file not in mywork/lab8 can be used

aws s3 presign --expires-in $EXPIRATION_TIME_SECONDS "s3://$BUCKET_NAME/$BASENAME"
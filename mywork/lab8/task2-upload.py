#!/usr/bin/env python
import boto3

s3 = boto3.client('s3', region_name='us-east-1')

bucket = 'ds2002-uak4ux'
local_file = 'friend.jpg'

with open(local_file, 'rb') as file:
    response = s3.put_object(
        Body = file,
        Bucket = bucket,
        Key = local_file, 
    )


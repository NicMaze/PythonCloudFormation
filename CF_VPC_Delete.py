#!/usr/bin/env python
import boto3
cf_client = boto3.client('cloudformation')
cf_client.delete_stack(
    StackName='NM-TEST',
)

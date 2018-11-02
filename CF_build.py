#!/usr/bin/env python
import boto3
cf_client = boto3.client('cloudformation')
cf_client.create_stack(
    StackName='NM-TEST',
    TemplateURL='https://s3-us-west-1.amazonaws.com/nm-cf-template-testing/StupidSimpleS3Bucket.yml',
    ResourceTypes=[
        'AWS::*'
    ],
    Tags=[
            {
                'Key': 'CreatedBy',
                'Value': 'NM'
            }
    ]
)

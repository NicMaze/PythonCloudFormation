#!/usr/bin/env python
import boto3
cf_client = boto3.client('cloudformation')
cf_client.create_stack(
    StackName='NM-TEST',
    TemplateURL='https://s3-us-west-1.amazonaws.com/nm-cf-template-testing/vpc_cs2.yml',
    ResourceTypes=[
        'AWS::*'
    ],
    Parameters=[
        {
            'ParameterKey': 'EnvironmentName',
            'ParameterValue': 'NM-TEMP-VPC',
        }
    ],
    Tags=[
            {
                'Key': 'CreatedBy',
                'Value': 'NM'
            }
    ]
)

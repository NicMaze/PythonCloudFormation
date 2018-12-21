import boto3
from botocore.exceptions import ClientError

###Global Variables###
ec2 = boto3.client('ec2')
securityGroupID = 'sg-0f9a8de0e20ff047b'
securityGroupID2nd = 'sg-951aebee'
validSG = []

def validateSG(securitySG):
    # validateSG takes the provided parameter (group-id) as an input and checks the SG for the department:security Tag. 
    # If the tag is not present on the provided group-id; the response is an empty list that returns "Invalid Security Group"
    # If the tag is present on the provided group-id; The group is appended to the validSG list and returns "Valid Security Group"
    # If we have to apply security groups we'll want a list of the valid ones.
    checkSG = ec2.describe_security_groups(Filters=[{'Name': 'group-id','Values': [securitySG,]}, {'Name': 'tag:department', 'Values': ['security']}])
    if checkSG['SecurityGroups'] == []:
        print("Invalid Security Group")
    else:
        validSG.append(securitySG)
        print("Valid Security Group")

# Feel free to ignore... useful to get some clean tests back though
print('****')
validateSG(securityGroupID)
validateSG(securityGroupID2nd)
print('****')
print(validSG)

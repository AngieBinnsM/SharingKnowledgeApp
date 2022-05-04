import os

import boto3
import pytest

from moto import mock_dynamodb

os.environ['DYNAMODB_TABLE'] = 'test-table'
os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'

@pytest.fixture(scope='function')
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ['AWS_ACCESS_KEY_ID'] = 'testing'
    os.environ['AWS_SECRET_ACCESS_KEY'] = 'testing'
    os.environ['AWS_SECURITY_TOKEN'] = 'testing'
    os.environ['AWS_SESSION_TOKEN'] = 'testing'

@pytest.fixture(scope='function')
def dynamodb(aws_credentials):
    with mock_dynamodb():
        conn = boto3.resource('dynamodb', region_name='us-east-1')
        yield conn

@pytest.fixture(scope='function')
def dynamodb_table(dynamodb):
    dynamodb.create_table(
        TableName= os.environ['DYNAMODB_TABLE'],
        KeySchema=[
            {
                'AttributeName': 'pk',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'sk',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'pk',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'sk',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
        }  
        )
        
    yield dynamodb
    
        

   
        

        
       
    
        
    
        

            
    
    
    
    


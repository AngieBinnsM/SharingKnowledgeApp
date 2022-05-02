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
def dynamodb_table(aws_credentials):
    
    with mock_dynamodb():
        table_name= os.environ["DYNAMODB_TABLE"]
        print(table_name)
        dynamodb = boto3.resource(
            'dynamodb', 
            region_name='us-east-1', 
            aws_access_key_id="ak",
            aws_secret_access_key="sk",
        )
        dynamodb.create_table(
        TableName= table_name,
        KeySchema=[
            {
                'AttributeName': 'PK',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'SK',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'PK',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'SK',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    
    yield dynamodb

            
    
    
    
    


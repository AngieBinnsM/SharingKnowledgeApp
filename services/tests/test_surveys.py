from conftest import dynamodb_table
from put_idea_test import handler
import boto3
import json
import os

# Event test
def to_item():
    test_event = {
        "body": json.dumps({
                "id": '1649426976418',
                "user": 'Raul',
                "technology": 'DynamoDB',
                "title": 'Single-Table Design with DynamoDB - Alex DeBrie, AWS Data Hero',
                "link": 'https://www.youtube.com/watch?v=BnDKD_Zv0og',
                "description": 'Its great for beginners'
            })
        }
        
    return test_event  

# Create a function to return a DynamoDB table to isolate the tests from live infrastructure.
def mocked_table():
    dynamodb = boto3.resource("dynamodb", region_name=os.environ['AWS_DEFAULT_REGION'])
    table = dynamodb.Table(os.environ["DYNAMODB_TABLE"])
    return table

#Test function
def test_create_survey(dynamodb_table):
    table = mocked_table()
    evento = to_item()
    

    assert handler(event= to_item(), table = table, context={}) == json.loads(evento['body'])

    respond = table.get_item(
            Key={
                "pk": "#Ideas",
                "sk": "#DynamoDB#1649426976418",
            }
        )
    assert respond["Item"] == {"pk": "#Ideas",
                "sk": "#DynamoDB#1649426976418",
                "id": '1649426976418',
                "user": 'Raul',
                "technology": 'DynamoDB',
                "title": 'Single-Table Design with DynamoDB - Alex DeBrie, AWS Data Hero',
                "link": 'https://www.youtube.com/watch?v=BnDKD_Zv0og',
                "description": 'Its great for beginners'}
    

    
    

    
    

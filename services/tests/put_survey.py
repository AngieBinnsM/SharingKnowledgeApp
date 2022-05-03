import os
import boto3
from moto import mock_dynamodb

# Create a function to return a DynamoDB table to isolate the tests from live infrastructure.
def get_Table():
    with mock_dynamodb():
        dynamo = boto3.resource("dynamodb", region_name= os.environ['AWS_DEFAULT_REGION'])
        table = dynamo.Table(os.environ["DYNAMODB_TABLE"])
        return table

#The function to test
def put_survey( survey=None, table = get_Table() ):
    try:
        table.put_item(
            Item=survey.to_item()
        )
        return survey

    except Exception as e:
        print("Error creating item")
        print(table)
        print(e)
        error_message = "Could not create item"
        return {
            "error": error_message
        }
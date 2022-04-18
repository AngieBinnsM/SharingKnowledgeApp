import boto3
from helper import (http_success, http_internal_error)
import json

def handler (event,context):
    print("event:", json.dumps(event))

    client = boto3.resource("dynamodb")
    table = client.Table('IdeasTable')

    try:
        technology = event['pathParameters']['technology']
        
        result = table.query(
            ExpressionAttributeValues={
                ':idea': "#Ideas",
                ':idea_technology': f"#{technology}"
            },
            KeyConditionExpression='pk=:idea and begins_with(sk, :idea_technology)',                 
        )

        ideas = result["Items"]

        return http_success(ideas)

    except:
        return http_internal_error()
import boto3
from helper import (http_success, http_internal_error)
import json

def handler (event,context):
    print("event:", json.dumps(event))

    client = boto3.resource("dynamodb")
    table = client.Table('IdeasTable')

    try:
        technology = event["queryStringParameters"]['technology']
        
        result = table.query(
            ExpressionAttributeValues={
                ':idea': "#Ideas",
                ':idea_technology': f"#{technology}"
            },
            KeyConditionExpression='pk=:idea and begins_with(sk, :idea_technology)',                 
        )

        ideas = result["Items"]

        ideas_response = []

        for idea in ideas:
            obj = {
                "id": idea["id"],
                "user": idea["user"],
                "technology": idea["technology"],
                "title": idea["title"],
                "link": idea["link"],
                "description": idea["description"]
            }
            ideas_response.append(obj)


        return http_success(ideas_response)

    except:
        return http_internal_error()
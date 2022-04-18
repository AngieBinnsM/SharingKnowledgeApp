import boto3
from helper import (http_success, http_internal_error)
import json

def handler (event,context):
    print("event:", json.dumps(event))

    client = boto3.resource("dynamodb")
    table = client.Table('IdeasTable')
    technology = event['pathParameters']['technology']

    try:
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

        response = {
            "ideas" : ideas_response
        }

        return http_success(response)

    except:
        return http_internal_error()
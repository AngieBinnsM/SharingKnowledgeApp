import boto3
from helper import (http_success, http_internal_error)
from boto3.dynamodb.conditions import Key

def handler(event, context):

    client = boto3.resource("dynamodb")
    table = client.Table('IdeasTable')

    try:
        result = table.query(
            KeyConditionExpression=Key('pk').eq("#Ideas")
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










   
import boto3
from helper import http_success,http_internal_error
import json

def handler (event,context):
    print("event:", json.dumps(event))

    client = boto3.resource("dynamodb")
    table = client.Table('IdeasTable')
    technology = event["queryStringParameters"]['technology']
    id = event["queryStringParameters"]['id']

    try:
        response = table.query(
            ExpressionAttributeValues={
                ':idea': "#Ideas",
                ':idea_id': f"#{technology}#{id}"
            },
            KeyConditionExpression='pk=:idea and begins_with(sk, :idea_id)'        
        )

        for item in response['Items']:
            table.delete_item(
                Key={
                    'pk': item['pk'],
                    'sk': item['sk']
                }
            )
        
        idIdea = {"id": id}

        return http_success(idIdea)

    except:
        return http_internal_error()
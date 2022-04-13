import boto3
from helper import http_success,http_internal_error


def handler (event,context):

    client = boto3.resource("dynamodb")
    table = client.Table('IdeasTable')
    id = event['queryStringParameters']['id']

    try:
        response = table.query(
            ExpressionAttributeValues={
                ':idea': "#Ideas",
                ':idea_id': f"#{id}"
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

        return http_success({'body':'Successfully deleted item!'})

    except:
        return http_internal_error()
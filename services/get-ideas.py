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

        return http_success(ideas)

    except:
        return http_internal_error()










   
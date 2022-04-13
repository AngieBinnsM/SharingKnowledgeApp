import json
import boto3
from helper import http_success,http_internal_error


def handler(event, context):

    client = boto3.resource("dynamodb")
    table = client.Table('IdeasTable')

    json_event = json.loads(event['body'])
    id = json_event['id']
    user = json_event['user']
    technology = json_event['technology']
    title = json_event['title']
    link = json_event['link']
    description = json_event['description']

    try:
        table.put_item(
            Item = {
                "pk": "#Ideas",
                "sk": f"#{id}#{technology}#{user}",
                "id": id,
                "user": user,
                "technology": technology,
                "title": title,
                "link": link,
                "description": description
            }
        )

    
        return http_success({'body':'Successfully added item!'})

    except:
        return http_internal_error()

        


import json
import boto3
from helper import http_success,http_internal_error


def handler(event, context):

    client = boto3.resource("dynamodb")
    table = client.Table('IdeasTable')

    json_event = json.loads(event['body'])
    id, user, technology, title, link, description = json_event.values()
    

    try:
        table.put_item(
            Item = {
                "pk": "#Ideas",
                "sk": f"#{technology}#{id}",
                "id": id,
                "user": user,
                "technology": technology,
                "title": title,
                "link": link,
                "description": description
            }
        )

        idea = {
                "id": id,
                "user": user,
                "technology": technology,
                "title": title,
                "link": link,
                "description": description
            }
        
        return http_success(idea)

    except:
        return http_internal_error()

        


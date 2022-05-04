import json

def handler(event, table, context ):

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
        
        return idea

    except:
        return False

        


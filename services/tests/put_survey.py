import os

#The function to test
def put_survey(survey=None, table=None):
    try:
        table.put_item(
            Item=survey.to_item()
        )
        return survey
    except Exception as e:
        print("Error creating item")
        print(e)
        error_message = "Could not create item"
        return {
            "error": error_message
        }
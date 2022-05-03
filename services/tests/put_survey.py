import os
import boto3


def get_Table():
    dynamo = boto3.resource("dynamodb", region_name= os.environ['AWS_DEFAULT_REGION'])
    table = dynamo.Table(os.environ["DYNAMODB_TABLE"])
    return table
        
default_table = get_Table()

#The function to test
def put_survey( survey=None, table = default_table ):
    try:
        table.put_item(
            Item=survey.to_item()
        )
        return survey

    except Exception as e:
        print("Error creating item")
        print(table)
        print(e)
        error_message = "Could not create item"
        return {
            "error": error_message
        }
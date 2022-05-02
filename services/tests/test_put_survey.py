import boto3
from put_survey import put_survey
import os

class StubSurvey:

    def __init__(self):
        pass
    
    def to_item(self):
        return {
            "PK": "CUSTOMER#TEST1",
            "SK": "SURVEY#TEST1",
            "customer_id": "TEST1",
            "survey_id": "TEST1",
            "survey_data": {"TEST": "DATA"}
        }

# Create a function to return a DynamoDB table to isolate the tests from live infrastructure.
def mocked_table():
    dynamodb = boto3.resource("dynamodb", region_name='us-east-1')
    table = dynamodb.Table(os.environ["DYNAMODB_TABLE"])
    return table

def test_create_survey():
    survey_instance = StubSurvey()
    table = mocked_table()
    assert put_survey(survey=survey_instance, table=table) == survey_instance

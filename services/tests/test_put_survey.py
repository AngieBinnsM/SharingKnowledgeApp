from put_survey import put_survey
from conftest import dynamodb_table
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


def test_create_survey(dynamodb_table):
    survey_instance = StubSurvey()
    assert dynamodb_table == True
    assert put_survey(survey=survey_instance) == survey_instance
    

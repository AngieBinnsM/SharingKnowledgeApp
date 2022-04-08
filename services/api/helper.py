import os
import json
import decimal

def decimal_to_str(obj):
    return str(obj)

def http_internal_error(event={}, origin="*"):
    return build_response("500", {"message": "Internal Server Error"}, origin)


def http_not_found(origin="*"):
    return build_response("404", {"message": "Item Not Found"}, origin)


def http_unauthorized(origin="*"):
    return build_response("403", {"message": "Unauthorized"}, origin)


def http_bad_request(origin="*"):
    return build_response("400", {"message": "Bad Request"}, origin)


def http_success(body, origin="*"):
    return build_response("200", body, origin)


def build_response(status_code, body, origin="*"):
    
    response = {
        "statusCode": status_code,
        "body": json.dumps(body, ensure_ascii=False, default=decimal_to_str),
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": origin,
            "Access-Control-Allow-Credentials": True,
        },
    }
    return response
import json


def hello(event, context):
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully... somehow...",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response


def byebye(event, context):
    body = {
        "message": "GoodBye...",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

import json
import boto3
from decimal import Decimal

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("user-table")


def default(o):
    if isinstance(o, Decimal):
        return int(o) if o % 1 == 0 else float(o)
    raise TypeError


def lambda_handler(event, context):
    user_id = int(event["pathParameters"]["user_id"])
    response = table.get_item(Key={"user_id": user_id})

    if "Item" not in response:
        return {
            "statusCode": 404,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"message": "User not found"}),
        }

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"user": response["Item"]}, default=default),
    }
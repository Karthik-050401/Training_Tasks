import json
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("user-table")


def lambda_handler(event, context):
    user_id = int(event["pathParameters"]["user_id"])

    response = table.delete_item(
        Key={
            "user_id": user_id
        },
        ReturnValues="ALL_OLD"
    )

    if "Attributes" not in response:
        return {
            "statusCode": 404,
            "body": json.dumps({
                "message": "User not found"
            })
        }

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "User deleted successfully",
            "user_id": user_id
        })
    }
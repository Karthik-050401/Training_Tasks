import json
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("user-table")

def lambda_handler(event, context):

    # Get user_id from the URL path
    user_id = int(event["pathParameters"]["user_id"])

    # Get update data from request body
    body = json.loads(event["body"])

    update_parts = []
    expression_values = {}

    if "name" in body:
        update_parts.append("name = :name")
        expression_values[":name"] = body["name"]

    if "age" in body:
        update_parts.append("age = :age")
        expression_values[":age"] = body["age"]
        
    if not update_parts:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": "Nothing to update"
            })
        }

    update_expression = "SET " + ", ".join(update_parts)

    response = table.update_item(
        Key={
            "user_id": user_id
        },
        UpdateExpression=update_expression,
        ExpressionAttributeValues=expression_values,
        ReturnValues="ALL_NEW"
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "User updated successfully",
            "user": response["Attributes"]
        }, default=str)
    }
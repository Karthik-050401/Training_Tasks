import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('user-table')

def lambda_handler(event, context):
    
    body = json.loads(event["body"])
    user_id = body["user_id"]
    name = body["name"]
    age = body["age"]

    table.put_item(
        Item={
            "user_id": user_id,
            "name": name,
            "age": age
        }
    )

    return {
        'statusCode': 201,
        'body' : json.dumps({
            "message" : "User created successfully",
            "user_id" : user_id
        })
    }
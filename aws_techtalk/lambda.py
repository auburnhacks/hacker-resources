import json
import boto3
from boto3.dynamodb.conditions import Attr
from decimal import *

def lambda_handler(event, context):
    score = event["params"]["path"]["score"]
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table("HackathonTest")
    
    if score == 'all':
        return table.scan()["Items"]
    elif score == 'range':
        # Return scores in the given range
        
        high = Decimal(str(event["params"]["querystring"]["high"]))
        low = Decimal(str(event["params"]["querystring"]["low"]))
        
        response = table.scan(
            FilterExpression=Attr('runtime').between(low, high)
        )
        
        return response["Items"]

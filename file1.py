import json

def lambda_handler(event, context):
    # TODO implement

    
    length = event['length']
    width = event['width']
    length = event['length']
    width = event['width']
    
    print(f"The area is {length}")
    print(f"The area is {width}")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


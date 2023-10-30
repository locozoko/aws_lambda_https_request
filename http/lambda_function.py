import requests

def lambda_handler(event, context):
    response = requests.get("http://ipinfo.io")
    return {
        "statusCode": response.status_code,
        "body": response.text
    }
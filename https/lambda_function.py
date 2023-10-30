import requests

def lambda_handler(event, context):
    url = 'https://ipinfo.io'
    cert_path = 'zscalerroot.pem'
    response = requests.get(url, verify=cert_path)
    return {
        "statusCode": response.status_code,
        "body": response.text
    }
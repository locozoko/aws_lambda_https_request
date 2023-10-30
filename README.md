# aws_lambda_https_request
Test making https calls with python lambda function that includes certificate for proxy ssl inspection
Both tests will conduct an http test using the requests python library to ipinfo.io

Instructions

1. Create 2 Python Lambda Functions (1 for http and 1 for https)
2. Configure the Lambda Functions to operate in a VPC/subnet that routes through Zscaler
3. Upload the http.zip file to the HTTP lambda function
4. Upload the https.zip file to the HTTPS lambda function
5. Ensure SSL inspection is enabled for this location/source in Zscaler
6. Run a Test on the HTTP lambda function. You should see a 200 response
7. Runa  Test on the HTTPS lamdbda function. You should see a 200 response
8. Check the Zscaler logs to verify/see the connections

* Note: You can replace the destinatino by modifying the lambda_function.py file in both HTTP and HTTPS to your desired destination
* Note: It is assumed the destination is allowed via Zscaler policies. If it is blocked the Test will return an expected failure.
* Note: This test includes the default Zscaler root certificate. If you use a custom enterprise/immediate cert in Zscaler instead of default, replace with yours

from __future__ import print_function
  
import json
import boto3
  
print('Loading function')
  
def lambda_handler(event, context):
  
    # Parse the JSON message 
    eventText = json.dumps(event)
  
    # Print the parsed JSON message to the console; you can view this text in the Monitoring tab in the Lambda console or in the CloudWatch Logs console
    print('Received event: ', eventText)
  
    # Create an SNS client.Since our demo needs SMS capability, need to set the region
    sns = boto3.client('sns', region_name='us-east-1')
    
    # Publish a message to the specified topic
    response = sns.publish (
      TopicArn = 'arn:aws:sns:us-east-1:474013637073:VasDemoNotificationTopic',
      Message = eventText
    )
  
    print(response)

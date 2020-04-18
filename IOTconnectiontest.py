# Chat application between cars

'''
* Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
*
* Licensed under the Apache License, Version 2.0 (the "License").
* You may not use this file except in compliance with the License.
* A copy of the License is located at
*
*  http://aws.amazon.com/apache2.0
*
* or in the "license" file accompanying this file. This file is distributed
* on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
* express or implied. See the License for the specific language governing
* permissions and limitations under the License.
'''

# Import the AWS IoT Device SDK
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

# Import json for parson endpoint.json file
import json

# Import os for finding name of current directory
import os

# Load the endpoint from file


# Fetch the deviceName from the current folder name
deviceName = os.path.split(os.getcwd())[1]



# Build useful variable for code
#subTopic = 'edx/messaging/' + deviceName
pubTopic = '$aws/things/Cam/shadow/update'
keyPath = 'E:\\iot\\private.pem.key'
certPath = 'E:\\iot\\certificate.pem.crt'
caPath = 'E:\\iot\\root-CA.crt'
clientId = deviceName
host = "a1350frjezi6ap-ats.iot.us-east-1.amazonaws.com"
port = 8883


# TODO 1: Use the AWSIoTMQTTClient library to create your AWSIoTMQTTClient 
#         client using the useful variable above and connect it to AWS IoT
myAWSIoTMQTTClient = AWSIoTMQTTClient(clientId)
myAWSIoTMQTTClient.configureEndpoint(host, port)
myAWSIoTMQTTClient.configureCredentials(caPath, keyPath, certPath)
myAWSIoTMQTTClient.connect()






# Function to publish payload to IoT topic
def publishToIoTTopic(topic, payload):
    # TODO 4: Implement function to publish to specified IoT topic using device object
    #         that you will create
    myAWSIoTMQTTClient.publish(topic, payload, 1)



#################################
# DON'T EDIT ANYTHING PAST THIS #
#################################
# Infinite loop reading console input and publishing what it finds
while True:
    publishToIoTTopic(pubTopic, "Hi")

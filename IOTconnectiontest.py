from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

import json

import os

deviceName = os.path.split(os.getcwd())[1]



pubTopic = '$aws/things/Cam/shadow/update'
keyPath = 'E:\\iot\\private.pem.key'
certPath = 'E:\\iot\\certificate.pem.crt'
caPath = 'E:\\iot\\root-CA.crt'
clientId = deviceName
host = "a1350frjezi6ap-ats.iot.us-east-1.amazonaws.com"
port = 8883


myAWSIoTMQTTClient = AWSIoTMQTTClient(clientId)
myAWSIoTMQTTClient.configureEndpoint(host, port)
myAWSIoTMQTTClient.configureCredentials(caPath, keyPath, certPath)
myAWSIoTMQTTClient.connect()

ini_string = {'Hi thing connection test': 1}

myAWSIoTMQTTClient.publish(pubTopic,json.dumps(ini_string), 1)

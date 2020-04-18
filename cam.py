from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import json
import os
import numpy as np
import cv2


deviceName = os.path.split(os.getcwd())[1]
ini_string = {'youre cam has deticted some movment ': 1} 

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

def publishToIoTTopic(topic, payload):
    
    myAWSIoTMQTTClient.publish(topic, payload, 1)

sdThresh = 10
font = cv2.FONT_HERSHEY_SIMPLEX
a=9
img_index=1
def distMap(frame1, frame2):
    """outputs pythagorean distance between two frames"""
    frame1_32 = np.float32(frame1)
    frame2_32 = np.float32(frame2)
    diff32 = frame1_32 - frame2_32
    norm32 = np.sqrt(diff32[:,:,0]**2 + diff32[:,:,1]**2 + diff32[:,:,2]**2)/np.sqrt(255**2 + 255**2 + 255**2)
    dist = np.uint8(norm32*255)
    return dist
 
cv2.namedWindow('frame')
cv2.namedWindow('dist')

cap = cv2.VideoCapture("http://192.168.43.1:8080/video")
 
_, frame1 = cap.read()
_, frame2 = cap.read()
 
facecount = 0
while(True):
    _, frame3 = cap.read()
    rows, cols, _ = np.shape(frame3)
    cv2.imshow('dist', frame3)
    dist = distMap(frame1, frame3)
 
    frame1 = frame2
    frame2 = frame3
 
    # apply Gaussian smoothing
    mod = cv2.GaussianBlur(dist, (9,9), 0)
     # apply thresholding
    _, thresh = cv2.threshold(mod, 100, 255, 0)
 
    # calculate st dev test
    _, stDev = cv2.meanStdDev(mod)
 
    cv2.imshow('dist', mod)
    cv2.putText(frame2, "Standard Deviation - {}".format(round(stDev[0][0],0)), (70, 70), font, 1, (255, 0, 255), 1, cv2.LINE_AA)
    if stDev > sdThresh:
            
            print("Motion detected.. Do something!!!")
            frame_name =("E:\\MOVMENT_RECORDED\\"+str(img_index)+str(".jpg"))
            cv2.imwrite(frame_name, frame2)
            print("saved", frame_name)
            img_index +=1
            a=a+1
            if a==10: 
                publishToIoTTopic(pubTopic,(json.dumps(ini_string)))
                a=0
            
 
    cv2.imshow('frame', frame2)
    if cv2.waitKey(1) & 0xFF == 27:
        break
 
cap.release()
cv2.destroyAllWindows()

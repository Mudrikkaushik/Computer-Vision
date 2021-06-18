import cv2
#import mediapipe as mp
import time
import Handsrecognition_Module as htm
import Pose_Det as pm


pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
detector = htm.handDetector()
detector1 = pm.poseDetector()
while True:
    success, img = cap.read()
    image = detector1.findPose(img)
    img = detector.findHands(img, draw=True )
    lmLists = detector1.findPosition(image, draw=False)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        print(lmList[4])
        #print(lmList[14])
        cv2.circle(img, (lmList[14][1], lmList[14][2]), 15, (0, 0, 255), cv2.FILLED)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    
'''while True:
    success, img = cap.read()
    img = detector1.findPose(img)
    lmList = detector1.findPosition(img, draw=False)
    if len(lmList) !=0:
        print(lmList[14])
        cv2.circle(img, (lmList[14][1], lmList[14][2]), 15, (0, 0, 255), cv2.FILLED)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)

    #cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
     #           (255, 0, 255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)'''

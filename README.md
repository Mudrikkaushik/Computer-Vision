<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![LinkedIn][linkedin-shield]][linkedin-url]
<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/MudrikKauhshik/Computer-Vision">
    <img src="https://user-images.githubusercontent.com/52999830/122551568-c5d68c80-d052-11eb-9b58-aa5bf3ec919e.png"
 alt="Logo" width="920" height="380">
  </a>
  <h3 align="center">Computer Vision with Mediapipe</h3>

  <p align="center">
    This is all about what I have learnt about the mediapipe so far Enjoy 😄.
    <br />
  </p>
</p>
<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#my-computer-vision-learnings-with-mediapipe">My Learning with Mediapipe</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#libraries-installation">Libraries Installation🕒</a></li>
        <li><a href="#hand-recogntion">Hand-Recogntion🖐</a></li>
        <li><a href="#pose-estimation">Pose-Estimation🏃‍♂️</a></li>
        <li><a href="#finger-counting">Finger-Counting👆✌✊</a></li>
        <li><a href="#volume-set">Volume-Set🎉</a></li>
        <li><a href="#contact">Contact😊</a></li>
      </ul>
    </li>
  </ol>
</details>
<!-- ABOUT THE PROJECT -->
## My Computer Vision Learnings with Mediapipe

![Capture](https://user-images.githubusercontent.com/52999830/122556272-eacdfe00-d058-11eb-8442-fa01f48e0ba2.gif)
![Caputure](https://google.github.io/mediapipe/images/mobile/hand_tracking_android_gpu_small.gif),![Caputure](https://google.github.io/mediapipe/images/mobile/face_mesh_android_gpu_small.gif),![Capture](https://google.github.io//mediapipe/images/mobile/holistic_tracking_android_gpu_small.gif),![Capture](https://google.github.io/mediapipe/images/mobile/face_detection_android_gpu_small.gif),![Capture](https://google.github.io/mediapipe/images/mobile/pose_tracking_android_gpu_small.gif)

MediaPipe is a prebuilt Python package on PyPI. It also provides tools for users to build their own solutions.MediaPipe Python package is available on PyPI for Linux, macOS and Windows.

Things that we can Perform with the help of Mediapipe
* Face Detection and Face Mesh
* Pose and Holistic Detection
* Object Detection and Tracking

In this Repository I have shred Following projects:
* Hand Recognition
* pose Estimation
* Finger Counting
* Volume Set

### Built With

The Prototype is made using as follows:
* Python
* Mediapipe
* Open CV
<!-- GETTING STARTED -->
## Getting Started

Initially Install all the necessary python libraries which are required .

### Libraries Installation
   ```sh
    import cv2 
    import os
    import mediapipe as mp
    import time
   ```
<!-- USAGE EXAMPLES -->
## Hand-Recogntion
First i have created a Scrypt which detect and tract the hands ,initially i have set the threshold to hands but we can laso edit that and increase the number of hands which has to be detect. I have also created a module of this project so that we dont have to write the whole code process again and  again in other projects like "Finger-Count".
![Capture](https://user-images.githubusercontent.com/52999830/122561180-2b307a80-d05f-11eb-914b-51b6e094197f.png)
```sh
import cv2
import mediapipe as mp
import time
import Handsrecognition_Module as htm

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    print(results.multi_hand_landmarks)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id,lm in results.enumerate(handLms.landmarks):
                #print(id,lm)
                h, w, c =img.shape
                cx, cy =int(lm.x*w),int(lm.y*h)
                print(id, cx, cy)
                if id==0:
                    cv2.circle(img,(cx,cy),15,(255,0,255),cv2.FILLED)
                
            mpDraw.draw_landmarks(img, handLms,mpHands.HAND_CONNECTIONS)
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
    
    cv2.imshow("Image",img)
    cv2.waitKey(1)
   ```
![Capture](https://user-images.githubusercontent.com/52999830/122562384-a3e40680-d060-11eb-9a98-46f9f23b1946.gif)
## Pose-Estimation
This project detect and tracks the position of the object.
I have tested it on both vedio Camera and mp4 files and they all seems to be working fine.
![Capture](https://user-images.githubusercontent.com/52999830/122634750-c6782d00-d0fd-11eb-814f-9e35d4cefd53.jpg)
 ```sh
 import cv2
import mediapipe as mp
import time
mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

cap =cv2.VideoCapture('3.mp4')
pT = 0 
while True:
    success, img = cap.read()
    imgRGB=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    #print(results.pose_landmarks)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img,results.pose_landmarks,mpPose.POSE_CONNECTIONS )
        for id,lm in enumerate(results.pose_landmarks.landmark):
            h,w,c=img.shape
            cx, cy =int(lm.x*w),int(lm.y*h)
            cv2.circle(img,(cx,cy),5,(255,0,0),cv2.FILLED)
            #print(id, cx, cy)
    cT =time.time()
    fps = 1/(cT-pT)
    pT = cT
    cv2.putText(img, str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
    cv2.imshow("Image",img)
    cv2.waitKey(1)
   ```
   ![Capture](https://user-images.githubusercontent.com/52999830/122634700-4d78d580-d0fd-11eb-86c4-043ca6c4fec4.gif)
## Finger-Counting
This project detect the fingers of the hand and also figures out how many finger does the user is pointing out.
the same technique can be appplied in order to detect the sign language.

  ![Capture](https://user-images.githubusercontent.com/52999830/122635231-4f906380-d100-11eb-9065-6fdc6d1abb0c.png)

 ```sh
 import cv2
import time
import os
import Handsrecognition_Module as htm

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

folderPath = "My_image"
myList = os.listdir(folderPath)
print(myList)
overlayList = []
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    # print(f'{folderPath}/{imPath}')
    overlayList.append(image)

print(len(overlayList))
pTime = 0

detector = htm.handDetector(detectionCon=0.75)

tipIds = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    # print(lmList)

    if len(lmList) != 0:
        fingers = []

        # Thumb
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # 4 Fingers
        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        # print(fingers)
        totalFingers = fingers.count(1)
        print(totalFingers)

        h, w, c = overlayList[totalFingers - 1].shape
        img[0:h, 0:w] = overlayList[totalFingers - 1]

        cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(totalFingers), (45, 375), cv2.FONT_HERSHEY_PLAIN,
                    10, (255, 0, 0), 25)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN,
                3, (255, 0, 0), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
   ```
   ![Capture](https://user-images.githubusercontent.com/52999830/122635354-05f44880-d101-11eb-99af-ddcf6d73d424.gif)
## Volume-Set
In this Volume set project I have integrated opencv with os so that i can alter my system's volume with the help of my hand Gestures.So in order to complete the proeject i have detemine andcreated a volume set landmark of the index finger and thumb finger because the distance between these two finger are maximum comparitively.
![Capture](https://user-images.githubusercontent.com/52999830/122635542-32f52b00-d102-11eb-8f4d-3061d15d4847.png)
 ```sh
import cv2
import time
import numpy as np
import Handsrecognition_Module as htm
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

################################
wCam, hCam = 640, 480
################################

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.handDetector(detectionCon=0.7)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# volume.GetMute()
# volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]
vol = 0
volBar = 400
volPer = 0
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        # print(lmList[4], lmList[8])

        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[20][1], lmList[20][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        cv2.circle(img, (x1, y1), 10, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
        cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)

        length = math.hypot(x2 - x1, y2 - y1)
        # print(length)

        # Hand range 50 - 300
        # Volume Range -65 - 0

        vol = np.interp(length, [50, 300], [minVol, maxVol])
        volBar = np.interp(length, [50, 300], [400, 150])
        volPer = np.interp(length, [50, 300], [0, 100])
        print(int(length), vol)
        volume.SetMasterVolumeLevel(vol, None)

        if length < 50:
            cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)

    cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (255, 0, 0), cv2.FILLED)
    cv2.putText(img, f'{int(volPer)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX,
                1, (255, 0, 0), 3)


    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX,
                1, (255, 0, 0), 3)

    cv2.imshow("Img", img)
    cv2.waitKey(1)
   ```
   ![Capture](https://user-images.githubusercontent.com/52999830/122635745-4228a880-d103-11eb-98e7-0200c5ffe153.gif)
   
 Hope you liked my Work,Leave a Star if you Do!
 Happy Learning😊😊😊
<!-- CONTACT -->
## Contact

Mudrik Kaushik - [Medium](https://mudrikkaushik.medium.com/) - [Gmail](https://mudrikkaushik@gmail.com/)

Prototype Link: [Click Here!](https://github.com/MudrikKauhshik/Image-Classifier)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/mudrik-kaushik/

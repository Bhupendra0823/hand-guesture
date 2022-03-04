import cv2
import mediapipe as mp
import time
import math
import numpy as np
import pyautogui
#################################
wscr,hscr=pyautogui.size()
wcam,hcam=640,480
length=0
pTime=0
cTime=0
smoothing=1
plocx,plocy=0,0
clocx,clocy=0,0
lmList=[]
finger=[]
tipIds=[4,8,12,16,20]
################################
cap=cv2.VideoCapture(0)
##############################################
mpHands =mp.solutions.hands
hands=mpHands.Hands()
mpDraw =mp.solutions.drawing_utils
##############################################
while True:
    sucess ,img =cap.read()
    img=cv2.resize(img,(720,480))
    img=cv2.flip(img,1)
    imgRGB=cv2.cvtColor(img ,cv2.COLOR_BGR2RGB)
    results=hands.process(imgRGB)
    if results.multi_hand_landmarks:
        myHand=results.multi_hand_landmarks[0]
        for handLms in results.multi_hand_landmarks:
            for id ,lm in enumerate(myHand.landmark):
                h, w , c =img.shape
                cx,cy=int(lm.x*w),int(lm.y*h)
                lmList.append([id,cx,cy])
###################################################################                
            if len(lmList)!=0:
                x1,y1=lmList[8][1:]
                x2,y2=lmList[12][1:]
            if lmList[tipIds[0]][1]>lmList[tipIds[0]-1][1]:
                finger.append(0)
            else:
                finger.append(1)
            for ids in range(1,5,):
                if lmList[tipIds[ids]][2]<lmList[tipIds[ids]-2][2]:
                    finger.append(1)
                else:
                    finger.append(0)
#########################################################################
            #cv2.rectangle(img,(100,100), (wcam-100 , hcam-100),(255,0,255),3)
            if (finger[1]==1 and finger[4]==1) and(finger[0]==0 and finger[2]==0 and finger[3]==0):
                st="yoo"
                cv2.putText(img,st,(10,70),cv2.FONT_HERSHEY_PLAIN,3,(225,0,0),3)
            if (finger[4]==1 and (finger[0]==0 and finger[1]==0 and finger[2]==0 and finger[3]==0)):
                cv2.putText(img,"Wash room",(10,70),cv2.FONT_HERSHEY_PLAIN,3,(225,0,0),3)
            if (finger[0]==1 and finger[1]==1 and finger[4]==1) and( finger[2]==0 and finger[3]==0):
                st="Love You"
                cv2.putText(img,st,(10,70),cv2.FONT_HERSHEY_PLAIN,3,(225,0,0),3)
            if finger[1]==0 and finger[0]==0 and finger[4]==0 and finger[2]==0 and finger[3]==0:
                cv2.putText(img,"Zero",(10,70),cv2.FONT_HERSHEY_PLAIN,3,(225,0,0),3)
            if (finger[1]==1 and (finger[0]==0 and finger[4]==0 and finger[2]==0 and finger[3]==0)):
                cv2.putText(img,"One",(10,70),cv2.FONT_HERSHEY_PLAIN,3,(225,0,0),3)
            if (finger[1]==1 and finger[2]==1 and (finger[4]==0 and finger[0]==0 and finger[3]==0)):
                cv2.putText(img,"Two",(10,70),cv2.FONT_HERSHEY_PLAIN,3,(225,0,0),3)
            if (finger[0]==0 and finger[4]==0 and (finger[1]==1 and finger[2]==1 and finger[3]==1)):
                cv2.putText(img,"Three",(10,70),cv2.FONT_HERSHEY_PLAIN,3,(225,0,0),3)
            if (finger[0]==0 and (finger[1]==1 and finger[4]==1 and finger[2]==1 and finger[3]==1)):
                cv2.putText(img,"Four",(10,70),cv2.FONT_HERSHEY_PLAIN,3,(225,0,0),3)
            if finger[1]==1 and finger[0]==1 and finger[4]==1 and finger[2]==1 and finger[3]==1:
                cv2.putText(img,"Five",(10,70),cv2.FONT_HERSHEY_PLAIN,3,(225,0,0),3)
            if finger[2]==1 and (finger[0]==0 and finger[1]==0 and finger[3]==0 and finger[4]==0):
                cv2.putText(img,"Fuck off",(10,70),cv2.FONT_HERSHEY_PLAIN,3,(225,0,0),3) 
                plocx,plocy=clocx,clocy
            finger=[]
            lmList=[]
#######################################################################################################
            mpDraw.draw_landmarks(img , handLms,mpHands.HAND_CONNECTIONS)
####################################################################################################        
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
#################################################################################################
    #cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
    cv2.imshow("Image" , img)
    cv2.waitKey(1)

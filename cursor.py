import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import autopy
import pyautogui as pui
import time

wCam, hCam = 640, 480
wS, hS = pui.size()
fR = 100
smootning = 7

cap = cv2.VideoCapture(0)

cap.set(3, wCam)
cap.set(4, hCam)
detector = HandDetector(detectionCon=0.7, maxHands=1)
pTime = 0
px, py = 0, 0
cur_x, cur_y = 0, 0


def mouseNclick(img, lmList):
    global px, py, cur_x, cur_y, fR, smootning, detector
    x1, y1 = lmList[8][:2]
    #x2, y2 = lmList[4][:2]
    fingers = detector.fingersUp(hands[0])

    #move
    if fingers[1] == 1:
        cor_x = np.interp(x1, (fR, wCam - fR), (0, wS))
        cor_y = np.interp(y1, (fR, hCam - fR * 2), (0, hS))

        cur_x = px + (cor_x - px) / smootning
        cur_y = py + (cor_y - py) / smootning
        try:
            autopy.mouse.move(cur_x, cur_y)
        except:
            pass

        cv2.circle(img, (x1, y1), 10, (255, 255, 0), cv2.FILLED)

        #double click
        if fingers[2]==1 and fingers[3]==1:
            pui.click(clicks=2)
            time.sleep(0.8)

        if fingers[2] == 1:
            #     #scroll
            #     if (py-cur_y) > 20:
            #         pui.scroll(30)
            #     if (py-cur_y) < -20:
            #         pui.scroll(-30)
            dis=detector.findDistance((x1,y1),(lmList[12][:2]))
            if dis[0] < 35:
                pamy = np.interp(y1, (fR, hCam - fR * 2), (0, hS))
                if pamy < 500:
                    pui.scroll(30)
                if pamy > 600:
                    pui.scroll(-30)

            else:
                #click
                if fingers[2]==1:
                    cv2.circle(img, (x1, y1), 10, (255, 0, 0), cv2.FILLED)
                    pui.click()
                    time.sleep(0.5)

        px, py = cur_x, cur_y

    # #scroll using palm
    # elif fingers == [0,0,0,0,0]:
    #     cv2.circle(img, (lmList[10][:2]), 10, (255, 0, 0), cv2.FILLED)
    #     pamy = np.interp(lmList[10][1], (fR, hCam - fR * 2), (0, hS))
    #     if pamy < 300:
    #         pui.scroll(30)
    #     if pamy > 1000:
    #         pui.scroll(-30)


while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False, draw=True)
    lmList = []
    cv2.rectangle(img, (fR - 50, fR - 50), (wCam - fR, hCam - fR * 2), (255, 255, 0), 2)

    if hands:
        lmList = hands[0]['lmList']
        bbox = hands[0]['bbox']
        #mouse click
        mouseNclick(img, lmList)

        cTIme = time.time()
        fps = 1 / (cTIme - pTime)
        pTime = cTIme
        cv2.putText(img, f'FPS: {int(fps)}', (35, 50), cv2.FORMATTER_FMT_C, 1, (255, 20, 230), 2)

    crop_image = img[(fR-50):(wCam-fR)][(fR-50):(hCam-fR*2)]
    cv2.imshow("Image", crop_image)
    cv2.setWindowProperty("Image", cv2.WND_PROP_TOPMOST,1)
    cv2.waitKey(1)


import pypylon.pylon as py
from PIL import Image
import cv2
import numpy as np
from matplotlib import pyplot as plt

camera = py.InstantCamera(py.TlFactory.GetInstance().CreateFirstDevice())
camera.Open()
camera.ExposureAuto.SetValue("Continuous")
camera.GainAuto.SetValue("Continuous")
camera.StartGrabbing(1)
grab = camera.RetrieveResult(2000, py.TimeoutHandling_ThrowException)

if grab.GrabSucceeded():
    img = grab.Array
    _,thresh1 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)

    contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    '''for i in contours:
        M = cv2.moments(i)
        if M['m00'] > 100000:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv2.drawContours(img, [i], -1, (0, 255, 0), 2)
            cv2.circle(img, (cx, cy), 7, (0, 0, 255), -1)
            cv2.putText(img, "center", (cx - 20, cy - 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
            break
    print(f"x: {cx} y: {cy}")'''

    for c in contours:
        area = cv2.contourArea(c)
        if (area>100000 and area<1000000):
            #x, y, w, h = cv2.boundingRect(c)
            #cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            (x,y),radius = cv2.minEnclosingCircle(c)
            center = (int(x),int(y))
            rad= int(radius)
            cv2.circle(img,center,rad,(0,255,0),2)
            print("dia in px value ",2*radius)
            print("dia of washer in mm scale: ", 2*rad*0.07)
            print("Center= X :",x,"Y:",y)


    #image_color = cv2.cvtColor(img, cv2.COLOR_BAYER_RG2BGR)
    #image = Image.fromarray(image_color)
    plt.imshow(img)
    #to calculate a point in the circumference use c1= x + r.cos(theta) and c2 = y + r.sin(theta)
    c1 = x + rad
    c2 = y 
    c3 = x - rad
    c4 = y
    plt.text(int(x)+35, int(y)+20, 'center', fontsize = 5)
    plt.text(int(c1)+35,int(c2)+20, 'p1',fontsize=5)
    plt.text(int(c3)-35,int(c4)-20, 'p2',fontsize=5)
    plt.text(800,0,f'Distance btw p1 & p2 in mm {2 * radius*0.07 }',fontsize=15)
    plt.plot(x,y,'ro',c1,c2,'ro',c3,c4,'ro')
    plt.plot([x,c1,c3],[y,c2,c4])
    
    plt.show()
    
    #image.show()
camera.close()

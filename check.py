import pypylon.pylon as py
from PIL import Image
import cv2
import numpy as np
from matplotlib import pyplot as plt

camera = py.InstantCamera(py.TlFactory.GetInstance().CreateFirstDevice())
camera.Open()
#camera.PixelFormat.SetValue("BayerRG8")
camera.ExposureAuto.SetValue("Continuous")
camera.GainAuto.SetValue("Continuous")
camera.AcquisitionMode.SetValue("Continuous")
camera.StartGrabbing(py.GrabStrategy_LatestImageOnly)

while camera.IsGrabbing():
    grab_result = camera.RetrieveResult(2000, py.TimeoutHandling_ThrowException)
    if grab_result.GrabSucceeded():
                
        img = grab_result.Array
        image_color = cv2.cvtColor(img, cv2.COLOR_BAYER_RG2BGR)
        image = Image.fromarray(image_color)
        #image.show()
    cv2.namedWindow('Image',cv2.WINDOW_NORMAL)
    cv2.imshow('Image', image_color)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
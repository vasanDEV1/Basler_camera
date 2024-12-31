#import necessary packages
import pypylon.pylon as py
from PIL import Image
import cv2
import numpy as np
from matplotlib import pyplot as plt

def main():
    # Initialize the camera
    camera = py.InstantCamera(py.TlFactory.GetInstance().CreateFirstDevice())
    camera.Open()
    camera.PixelFormat.SetValue("BayerRG8")
    camera.ExposureAuto.SetValue("Continuous")
    camera.GainAuto.SetValue("Continuous")
    camera.AcquisitionMode.SetValue("Continuous")
    camera.StartGrabbing(py.GrabStrategy_LatestImageOnly)

    try:
        while camera.IsGrabbing():
            grab_result = camera.RetrieveResult(2000, py.TimeoutHandling_ThrowException)
            if grab_result.GrabSucceeded():
                
                img = grab_result.GetArray()

                
                _, thresh2 = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)

                
                contours, hierarchy = cv2.findContours(thresh2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

                
                for contour in contours:
                    x, y, w, h = cv2.boundingRect(contour)
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

                
                #cv2.imshow('Thresholded Image', thresh2)
                cv2.namedWindow('Image',cv2.WINDOW_NORMAL)
                cv2.imshow('Image', img)

                
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            grab_result.Release()  

    except Exception as e:
        print(f"An error has occurred: {e}")

    finally:
        
        camera.StopGrabbing()
        camera.Close()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

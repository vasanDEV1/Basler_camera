import cv2
import numpy as np
import pypylon.pylon as py

def main():
    camera = py.InstantCamera(py.TlFactory.GetInstance().CreateFirstDevice())
    camera.Open()
    camera.AcquisitionMode.SetValue("Continuous")
    camera.StartGrabbing(py.GrabStrategy_LatestImageOnly)
    Low_limit = np.array([98,50,50])
    Up_limit = np.array([139,255,255])

    try:

        while camera.IsGrabbing():
            grab = camera.RetrieveResult(2000, py.TimeoutHandling_ThrowException)
            
            if grab.GrabSucceeded():
            
                img = grab.Array
                image_color = cv2.cvtColor(img, cv2.COLOR_BAYER_RG2RGB)
                hsv=cv2.cvtColor(image_color,cv2.COLOR_BGR2HSV)
                blue_mask = cv2.inRange(hsv,Low_limit,Up_limit)
                
                blue=cv2.bitwise_and(image_color,image_color,mask=blue_mask)
                cv2.namedWindow('Blue Filter',cv2.WINDOW_NORMAL)
                cv2.imshow('Blue Filter',blue)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            grab.Release()
    except Exception as e:
        print(f"An error has occurred: {e}")
    finally:
        camera.StopGrabbing()
        camera.Close()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

import os
from datetime import datetime
import cv2


def check_directory(directory_name):
    directory_path = os.path.abspath(os.path.join(os.path.dirname(__file__), directory_name))
    if os.path.exists(directory_path):
        image_path =  os.path.join(directory_path, directory_name)
        return image_path
    else:
        os.mkdir(directory_name)
        image_path =  os.path.join(directory_path, directory_name)
        return image_path


def on_camera():
    camera_on = True
    cam = cv2.VideoCapture (0)
    while camera_on:
            ret, img =cam.read()
            cv2.imshow("webcam",img)
            if not ret:
                break;
            k=cv2.waitKey(10)
            if k%256 == 27:
                print("Closing...")
                break;
            elif k%256 == 32:

                timestamp = datetime.now().strftime ("%Y-%m-%d_%H-%M-%S")
                filename = f"image_{timestamp}.jpg"
                file = check_directory("images")+filename
                cv2.imwrite(file,img)
                camera_on = False

    cam.release()
    cv2.destroyAllWindows()

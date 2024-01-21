import cv2
cam = cv2.VideoCapture(0)
img_counter=0


camera_on = True
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
            print("Image " +str(img_counter)+"saved")
            file = 'C:/Users/alhar/Desktop/Project/strabismus/Strabismus-Detection-Mediapipe-main/Images'+str(img_counter)+'.jpg'
            cv2.imwrite(file,img)
            img_counter += 1
            camera_on = False

cam.release()
cv2.destroyAllWindows()

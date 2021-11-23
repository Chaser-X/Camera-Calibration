import cv2

camera:cv2.VideoCapture = cv2.VideoCapture(0)
num = 0 
while(1):
    ret, img = camera.read()
    cv2.imshow("test",img)

    if cv2.waitKey(10)&0xff == ord('s'):
        num += 1
        filename = "./CalImage/cal" + str(num) + ".jpg"
        cv2.imwrite(filename, img)
        print(filename + " saved!")
    if cv2.waitKey(10)&0xff == ord('q'):
        cv2.destroyAllWindows()
        camera.release()
        break


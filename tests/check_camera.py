import cv2, argparse

parser = argparse.ArgumentParser()
parser.add_argument("--camid", type=int, default=0)
args   = parser.parse_args()

cap = cv2.VideoCapture(args.camid)
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('Webcam Live', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()

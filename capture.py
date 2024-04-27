import cv2

def capture_video():
    cap = cv2.VideoCapture(1)

    while True:
        ret, frame = cap.read()
        if not ret: 
            print("Failed to grab frame")
            break

        frame = cv2.flip(frame,1)

        cv2.imshow('Video Capture', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_video.video()
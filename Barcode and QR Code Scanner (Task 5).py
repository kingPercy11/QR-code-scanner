import cv2
from pyzbar.pyzbar import decode
import webbrowser


def barcode_scanner(input):
    decoded_objects = decode(input)
    for obj in decoded_objects:
        data = obj.data.decode("utf-8")
        barcode_type = obj.type
        print(f"Type: {barcode_type}, Data: {data}")
        webbrowser.open(data)

def scan_codes(input_type, input_path):
    cap = None
    if input_type == 0:
        cap = cv2.VideoCapture(0)
    elif input_type == 1:
        image = cv2.imread(input_path)
    elif input_type == 2:
        cap = cv2.VideoCapture(input_path)
    else:
        print("Invalid input type.")
        return
    while True:
        if cap is not None and (input_type == 0 or input_type == 2):
            while True:
                ret, frame = cap.read()
                barcode_scanner(frame)
                if not ret:
                    print("webcam or video file not working")
                    break
                cv2.imshow('Camera Test', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        elif input_type == 1:
            frame = image.copy()
            gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            barcode_scanner(gray_image)
        else:
            print("Invalid input type.")
        break
    if cap is not None and (input_type == 0 or input_type == 2):
        cap.release()
    cv2.destroyAllWindows()


input_type = int(input("Enter the input type (0 for camera, 1 for image, 2 for video): "))
input_path = ""
if input_type == 1 or input_type == 2:
    input_path = input("Enter the path to your image or video: ")
scan_codes(input_type, input_path)

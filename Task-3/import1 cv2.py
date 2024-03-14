import cv2

# Path to the Haar cascade classifier XML file
harcascade = r"D:\Python\TASKPY\Task-3\harcascade_frontalface_default (1).xml"

# Create cascade classifiers for face detection
facecascade = cv2.CascadeClassifier(harcascade)

# Open the webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Set width
cap.set(4, 480)  # Set height

while True:
    # Read frame from the webcam
    success, img = cap.read()
    
    # Convert the frame to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the grayscale frame
    faces = facecascade.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=4)
    
    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)  
    
    # Display the frame with rectangles drawn around faces
    cv2.imshow("Face Detection", img)    
    
    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

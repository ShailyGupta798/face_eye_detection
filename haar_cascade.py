import cv2
#different cascade files are available for different purposes, face and eye are used here.
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0) # start the camera
while 1:                 #for continuous loop
    ret, img = cap.read() #inputs from the camera
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #converting colored image to gray scale since easy to use.
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) #detect faces
    #creating rectangular box around face and setting region of image(ROI) for eyes
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray) #detect eyes
        #creating rectangle around eyes
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            cv2.imshow('img',img)
    #for exiting the window press "q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
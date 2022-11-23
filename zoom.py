# imports
import numpy as np
from PIL import Image
import cv2
import time

# initializations
face_cascade = cv2.CascadeClassifier('cascades\data\haarcascade_frontalface_default.xml')
capture = cv2.VideoCapture(0)

# settings
RESOLUTION = (640,480)
face_memory = 10 

# declarations
past_frame = []
previous_faces = []
skip_counter = 0

# goes through previous faces, returns most recent, or empty list if none
def check_previous_faces(previous_faces):
    prev = previous_faces[::-1]
    for i in previous_faces:
        if i != []:
            return i
    return []

# sets size to resolution set at settings at top
def rescale_frame(frame):
    width = int(RESOLUTION[0])
    height = int(RESOLUTION[1])
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

# main code
if __name__ == "__main__":
    while True:
        # create frame, get faces with cascade (using grayscale frame)
        ret, frame = capture.read()
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor = 1.5, minNeighbors = 5)

        # store previous faces, reduce length of list to number set in settings
        if len(faces) > 0:
            previous_faces.append(faces)
        else:
            previous_faces.append([])

        if len(previous_faces) > face_memory:
            previous_faces = previous_faces[-face_memory:]

        # if face exists, zoom into it
        for (x,y,w,h) in faces:
            try:
                roi_color = frame[y-(h//4):y+h + (h//4), x-(w//4):x+w + (w//4)]
                past_frame = roi_color
                lockStart = time.time()
            except:
                roi_color = frame[x,y,x+w,y+h]

            if faces != (): 
                frame = roi_color

        # temp is the most recent possible face
        temp = check_previous_faces(previous_faces)
        try:
            # try showing one of these frames
            # first account for any errors, show the last frame
            if (w < 30 and h < 30) or (len(faces) > 1):
                cv2.imshow('frame', rescale_frame(past_frame))
            else:
                # otherwise show the possible previous faces, else show the full frame
                try: 
                    cv2.imshow('frame', rescale_frame(temp))
                except: 
                    cv2.imshow('frame', rescale_frame(frame))
    
        except: 
            # will occur when face is near edge of screen, comment out to see # of skips
            # skip_counter += 1
            # print(f"{skip_counter} frames skipped.")
            pass

        # close program with space key
        if cv2.waitKey(20) & 0xFF == ord(' '):
            break

    cv2.destroyAllWindows()
    print("FaceZoom ended successfully.")
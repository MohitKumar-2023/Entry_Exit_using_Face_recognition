import face_recognition as fr
import cv2 as cv
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os

Tk().withdraw()
load_image = askopenfilename()

name = input('Enter the entry number: ')

target_image = fr.load_image_file(load_image)
target_encoding = fr.face_encodings(target_image)

def find_target_face():
    face_location = fr.face_locations(target_image)
    folder = 'people/'
    filename = name+'.jpg'
    known_image = fr.load_image_file(f'{folder}{filename}')
    encoded_face = fr.face_encodings(known_image)[0]

    is_target_face = fr.compare_faces(encoded_face, target_encoding, tolerance=0.55)

    no_face = 1
    for i,face_match in enumerate(is_target_face):
        if face_match:
            no_face = 0
            create_frame(face_location[i], name)

    if no_face==1:
        print('Person with given entry number is not present. ')
        exit(0)

    print(f'{is_target_face} {name}')

def create_frame(location, label):
    top, right, bottom, left = location

    cv.rectangle(target_image, (left,top), (right, bottom), (255,0,0), 2)
    cv.rectangle(target_image, (left,bottom + 20), (right,bottom), (255,0,0), cv.FILLED)
    cv.putText(target_image, label, (left+3,bottom+14), cv.FONT_HERSHEY_DUPLEX, 0.4, (255,255,255), 1)

def render_image():
    rgb_img = cv.cvtColor(target_image, cv.COLOR_BGR2RGB)
    cv.imshow('Face Recognition', rgb_img)
    cv.waitKey(0)

find_target_face()
render_image()
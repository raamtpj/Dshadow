# Computer script for recognising input devices 
# 
# MIT License
# 
# Copyright (c) 2023 M.V.Raam Kumar
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from teachable_machine import TeachableMachine
import cv2 as cv
import serial, easyocr

img_mdl = TeachableMachine(model_path="..\\data\\imgr\\keras_model.h5",
                         labels_file_path="..\\data\\imgr\\labels.txt")

image_path = "img.jpg"
SERIAL = "COM4"
port = serial.Serial(SERIAL, baudrate="115200")

def get_image():
    cam = cv.VideoCapture(0)
    _, img = cam.read()
    cv.imwrite(image_path, img)

def image_recognition():
    result = img_mdl.classify_image(image_path)
    face = str(result["highest_class_id"]) + '\r\n'
    port.write(face.encode())

def read_image():
    reader = easyocr.Reader(['en'])
    res = reader.readtext(image_path, detail=0)
    res = ' '.join(res) + '\r\n'
    port.write(res.encode())


print("Dshadow slave program started")

while True:
    cmd = port.readline().decode().rstrip()
    if cmd == "IMG RECR":
        get_image()
        image_recognition()
    elif cmd == "IMG RD":
        get_image()
        read_image()
    elif cmd == "OBJ SNS":
        port.write("Not yet Implemented".encode())
    elif cmd == "EXIT":
        print("Program Halted by Micro:bit")
        break
    else:
        port.write("Invalid".encode())
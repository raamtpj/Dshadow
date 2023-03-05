from microbit import *
from speech import say

face_names = {
    "0": "Raam",
    "1": "Harish",
    "2": "Venkatesan",
    "3": "Abdul Kalam sir",
    "4": "Bill Gates sir",
    "5": "MS Dhoni"
}

def speak(txt):
    say(txt, speed=92, pitch=69, throat=188, mouth=455)

uart.init(baudrate=115200)
speak("welcome to DELTASHADOW")

while True:
    if button_a.is_pressed():
        print("IMG RECR")
        speak("Image. recognition. ON.")
        faceno = uart.readline()
        if faceno:
            faceno = str(faceno.decode('utf8').rstrip())
            text = "I saw " + face_names[faceno]
            speak(text)
    elif button_b.is_pressed():
        print("IMG RD")
        speak("Image. reading. ON.")
        sleep(4000)
        text = uart.readline()
        if text:
            text = str(text.decode('utf8').rstrip())
            display.scroll(text)
            speak(text)
    elif pin_logo.is_touched():
        print("EXIT")
        speak("Program. Halted.")
    
    while uart.any():
        uart.read()

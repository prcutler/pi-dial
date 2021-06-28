
from gpiozero import Button, RotaryEncoder
from threading import Event


mute_button = Button(13)

while True:
    if mute_button.is_pressed:
        print("Button is pressed")
    else:
        print("Button is not pressed")

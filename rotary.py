import denonavr
from gpiozero import Button, RotaryEncoder
from threading import Event

# GPIO pints in use
mute_button = Button(13)

# Set Denon AVR stats
zones = {"Zone2": "Paul Office"}
rec = denonavr.DenonAVR("192.168.1.119", name="Main Zone", add_zones=zones)
rec.async_setup()
rec.async_update()

# receiver = rec.zones['Zone2']
print(rec.zones['Zone2'].mute, rec.zones['Zone2'].volume)
#print(rec.zones)

rec.zones['Zone2'].async_mute(False)
rec.async_update()



while True:
    if mute_button.is_pressed:
        if rec.zones['Zone2'].mute is None:
            rec.zones['Zone2'].mute(False)
            print("Turning off mute")
            rec.async_update()
        else:
            rec.zones['Zone2'].mute(True)
            print("Muting")
            rec.async_update()
    else:
        pass




#while True:
#    if mute_button.is_pressed:
#        print("Button is pressed")
#    else:
#        print("Button is not pressed")

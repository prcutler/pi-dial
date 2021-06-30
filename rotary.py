import denonavr
from gpiozero import Button, RotaryEncoder
from threading import Event
from signal import pause

# GPIO pints in use
mute_button = Button(13)

# Set Denon AVR stats
zones = {"Zone2": "Paul Office"}
rec = denonavr.DenonAVR("192.168.1.119", name="Main Zone", add_zones=zones)
rec.update()
rec.zones['Zone2'].update()

# receiver = rec.zones['Zone2']
print(rec.zones['Zone2'].input_func, rec.zones['Zone2'].volume)
#print(rec.zones)

rec.zones['Zone2'].mute(False)
rec.zones['Zone2'].update()
print("Zone 2 mute status is: ",rec.zones['Zone2'].muted)

## This mutes but does not un-mute
def mute_receiver():
    print("mute status: ", rec.zones['Zone2'].muted)
    
    if rec.zones['Zone2'].muted is True:
        print("Receiver is muted already!")
        rec.zones['Zone2'].mute(False)
        rec.zones['Zone2'].update()
        print("Turned off mute")
        print("mute status after turned off mute: ", rec.zones['Zone2'].muted)
        
    else:
        print("muted false, try to unmute")
        rec.zones['Zone2'].mute(True)
        rec.zones['Zone2'].update()
        print("Muting")
     

mute_button.when_pressed = mute_receiver

pause()

## while loop works to turn mute on, but not off:

#while True:
#    if mute_button.when_pressed:
#        if rec.zones['Zone2'].mute is True:
#            rec.zones['Zone2'].mute(False)
#            print("Turning off mute")
#            rec.async_update()
#        else:
#            rec.zones['Zone2'].mute(True)
#            print("Muting")
#            rec.async_update()
#    else:
#        pass



#while True:
#    if mute_button.is_pressed:
#        print("Button is pressed")
#    else:
#        print("Button is not pressed")

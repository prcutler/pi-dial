from gpiozero import Button, RotaryEncoder
from threading import Event
import denonavr

# GPIO pints in use
mute_button = Button(13)

# Set Denon AVR stats
zones = {"Zone2": "Paul Office"}
rec = denonavr.DenonAVR("192.168.1.119", name="Main Zone", add_zones=zones)
rec.update()
rec.zones['Zone2'].update()

# At startup, print what input Zone 2 is on and what the volume is currently set to
print(rec.zones['Zone2'].input_func, rec.zones['Zone2'].volume)

# At startup, turn mute off on Zone 2
rec.zones['Zone2'].mute(False)
rec.zones['Zone2'].update()
print("Zone 2 mute status is: ",rec.zones['Zone2'].muted)

print("mute status: ", rec.zones['Zone2'].muted)

def mute_switch():
    while True:
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

if __name__ == "__main__":
    mute_switch()

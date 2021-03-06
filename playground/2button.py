import denonavr
from gpiozero import RotaryEncoder, Button
from signal import pause

# button-test.py will be used to test the pigpio_encoder library and rotary.py uses gpiozero

# Set Denon AVR stats and connect to AVR Zone 2
zones = {"Zone2": "Paul Office"}
rec = denonavr.DenonAVR("192.168.1.119", name="Main Zone", add_zones=zones)
rec.update()
rec.zones["Zone2"].update()

# At startup, print what input Zone 2 is on and what the volume is currently set to
print(rec.zones["Zone2"].input_func, rec.zones["Zone2"].volume)

# At startup, turn mute off on Zone 2 and show current status
rec.zones["Zone2"].mute(False)
rec.zones["Zone2"].set_volume(-40.0)
rec_volume = float(rec.zones["Zone2"].volume)
rec.zones["Zone2"].update()
print("Zone 2 mute status is: ", rec.zones["Zone2"].muted)
print("mute status: ", rec.zones["Zone2"].muted)
print("Volume is: ", rec.zones["Zone2"].volume, type(rec.zones["Zone2"].volume))


def volume_knob():

    rotor = RotaryEncoder(5, 6, wrap=False, max_steps=60)
    print("rotor step starts at: ", rotor.max_steps)
    rotor.steps = rec_volume
    mute_button = Button(13)

    while True:

        def volume_up():
            louder_steps = rotor.steps
            rec.zones["Zone2"].volume_up()
            rec.zones["Zone2"].update()
            print("Turned it up this much: ", louder_steps)

        def volume_down():
            # softer = (rotor.steps + 180) / 360
            softer_steps = rotor.steps
            rec.zones["Zone2"].volume_down()
            rec.zones["Zone2"].update()
            print("Turned it down this much: ", softer_steps)

        def press_mute():
            if rec.zones["Zone2"].muted is True:
                print("Receiver is muted already!")
                rec.zones["Zone2"].mute(False)
                rec.zones["Zone2"].update()
                print("Turned off mute")
                print("mute status after turned off mute: ", rec.zones["Zone2"].muted)

            else:
                print("muted false, try to unmute")
                rec.zones["Zone2"].mute(True)
                rec.zones["Zone2"].update()
                print("Muting")
                print("Mute Engaged")

        rotor.when_rotated_clockwise = volume_up

        rotor.when_rotated_counter_clockwise = volume_down

        mute_button.when_pressed = press_mute

        pause()

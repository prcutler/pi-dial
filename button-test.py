from signal import pause

import denonavr
from gpiozero import Button, RotaryEncoder

# button-test.py will be used to test the pigpio_encoder library and rotary.py uses gpiozero

# Set Denon AVR stats and connect to AVR Zone 2
zones = {"Zone2": "Paul Office"}
rec = denonavr.DenonAVR("192.168.1.119", name="Main Zone", add_zones=zones)
rec.update()
rec.zones["Zone2"].update()

# At startup, print what input Zone 2 is on and what the volume is currently set to
print(
    "Startup info for Zone2 is ",
    rec.zones["Zone2"].input_func,
    rec.zones["Zone2"].volume,
)

# At startup, turn mute off on Zone 2 and show current status
rec.zones["Zone2"].mute(False)
rec.zones["Zone2"].set_volume(-40.0)
rec_volume = float(rec.zones["Zone2"].volume)
rec_input = rec.zones["Zone2"].input_func
rec.zones["Zone2"].update()
print("Zone 2 mute status is: ", rec.zones["Zone2"].muted)
print("Volume is: ", rec.zones["Zone2"].volume, type(rec.zones["Zone2"].volume))


# Set Denon AVR stats
zones = {"Zone2": "Paul Office"}
rec = denonavr.DenonAVR("192.168.1.119", name="Main Zone", add_zones=zones)
rec.update()
rec.zones["Zone2"].update()

zone2_volume = rec.zones["Zone2"].volume
zone2_input = rec.zones["Zone2"].input_func
print("Zone 2 INPUT IS: ", zone2_input, type(zone2_input))


def volume_knob():

    # Rotor #1 is used to change volume and mute on / off
    volume_rotor = RotaryEncoder(5, 6, wrap=False, max_steps=60)
    print("rotor step starts at: ", volume_rotor.max_steps)
    volume_rotor.steps = rec_volume
    mute_button = Button(13)

    # Rotor #2 is used to change volume and mute on / off
    input_rotor = RotaryEncoder(19, 26, wrap=False, max_steps=60)
    print("rotor step starts at: ", input_rotor.max_steps)
    input_rotor.steps = zone2_input
    power_button = Button(21)

    while True:

        def volume_up():
            louder_steps = volume_rotor.steps
            rec.zones["Zone2"].volume_up()
            rec.zones["Zone2"].update()
            print("Turned it up this much: ", louder_steps)

        def volume_down():
            # softer = (rotor.steps + 180) / 360
            softer_steps = volume_rotor.steps
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

        def input_rotor():
            input_up = input.rotor.steps
            rec.zones["Zone2"].volume_up()
            rec.zones["Zone2"].update()
            print("Turned it up this much: ", input_up)

        input_rotor.when_rotated_clockwise = input_rotor

        volume_rotor.when_rotated_clockwise = volume_up

        volume_rotor.when_rotated_counter_clockwise = volume_down

        mute_button.when_pressed = press_mute

        pause()


def mute_switch():
    while True:
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


def input_switch():

    rotor = RotaryEncoder(5, 6, wrap=False, max_steps=60)

    rotor.steps = int(len(rec.input_func_list))
    print(rotor.steps)

    # TODO Define type of rotor.steps

    while True:

        def input_up():
            current_input = rec.input_func

            input_up_steps = rotor.steps

            for input in range(0, len(rec.input_func_list)):
                if rec.input_func_list[input] == current_input:
                    rec.input_func_list[input].index += 1
                    rec.update()
                    print("Current input is: ", rec.input_func)

        def input_down():
            current_input = rec.input_func

            input_down_steps = rotor.steps

            for input in range(0, len(rec.input_func_list)):
                if rec.input_func_list[input] == current_input:
                    rec.input_func_list[input].index -= 1
                    rec.update()
                    print("Current input is: ", rec.input_func)

        rotor.when_rotated_clockwise = input_up
        rotor.when_rotated_counter_clockwise = input_down

        pause()


if __name__ == "__main__":
    volume_knob()
    # input_switch()

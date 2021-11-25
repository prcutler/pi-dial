from signal import pause
from time import sleep
import denonavr
from gpiozero import Button, RotaryEncoder


# List of inputs on the receiver that need to be skipped  (8k and bluetooth)
bad_input_list = [0, 3, 7]

# Set Denon AVR stats and connect to AVR Zone 2
zones = {"Zone2": "Paul Office"}
rec = denonavr.DenonAVR("192.168.1.119", name="Main Zone", add_zones=zones)
rec.update()
rec.zones["Zone2"].update()

# At startup, print what input Zone 2 is on and what the volume is currently set to
# print("Startup info for Zone2 is ",
rec.zones["Zone2"].input_func
rec.zones["Zone2"].volume

# At startup, turn mute off on Zone 2 and show current status
rec.zones["Zone2"].mute(False)
rec.zones["Zone2"].set_volume(-40.0)
rec_volume = float(rec.zones["Zone2"].volume)
rec_input = rec.zones["Zone2"].input_func
rec.zones["Zone2"].update()
# print("Zone 2 mute status is: ", rec.zones["Zone2"].muted)
# print("Volume is: ", rec.zones["Zone2"].volume, type(rec.zones["Zone2"].volume))

# Zone 2 information
zone2_volume = rec.zones["Zone2"].volume
zone2_input = rec.zones["Zone2"].input_func
zone2_input_list = rec.zones["Zone2"].input_func_list
# print("All inputs: ", zone2_input_list)
# print("Zone 2 INPUT IS: ", zone2_input)

# Connect to the Rotary Encoders connected to the Raspberry PI
# Rotary Encoder 1
volume_rotor = RotaryEncoder(5, 6, wrap=False, max_steps=60)
volume_rotor.steps = rec_volume
mute_button = Button(13)
# Rotary Encoder 2
input_rotor = RotaryEncoder(26, 19, wrap=True, max_steps=24)
# print("rotor step starts at: ", input_rotor.max_steps)
input_rotor.steps = len(zone2_input_list)
# print(zone2_input, type(zone2_input), zone2_input_list.index(zone2_input))

# See README for how you can make the power button work automagically
# See also: https://embeddedpi.com/documentation/gpio/mypi-industrial-raspberry-pi-psu-shutdown-gpio-line
# power_button = Button(21)


def pi_dial():
    def volume_up():
        louder_steps = volume_rotor.steps
        rec.zones["Zone2"].volume_up()
        rec.zones["Zone2"].update()
        # print("Turned it up this much: ", louder_steps)

    def volume_down():
        softer_steps = volume_rotor.steps
        rec.zones["Zone2"].volume_down()
        rec.zones["Zone2"].update()
        # print("Turned it down this much: ", softer_steps)

    def press_mute():
        if rec.zones["Zone2"].muted is True:
            # print("Receiver is muted already!")
            rec.zones["Zone2"].mute(False)
            rec.zones["Zone2"].update()
            # print("Turned off mute")
            # print("mute status after turned off mute: ", rec.zones["Zone2"].muted)

        else:
            # print("muted false, try to unmute")
            rec.zones["Zone2"].mute(True)
            rec.zones["Zone2"].update()
            # print("Muting")
            # print("Mute Engaged")

    def input_change(inp_dir):
        current_input = rec.zones["Zone2"].input_func
        curr_pos = zone2_input_list.index(current_input)

        if inp_dir == 1:
            if curr_pos == 12:
                new_index = 0
            else:
                new_index = curr_pos + 1

            while new_index in bad_input_list:
                new_index += 1
                if new_index >= 13:
                    new_index = 0
        else:
            if curr_pos == 0:
                new_index = 12
            else:
                new_index = curr_pos - 1

            # take care of the spots where it gets stuck, possibly due to non-existent receiver inputs
            while new_index in bad_input_list:
                new_index -= 1
                if new_index <= 0:
                    new_index = 12

        new_index_name = zone2_input_list[new_index]
        rec.zones["Zone2"].set_input_func(new_index_name)
        rec.zones["Zone2"].update()
        sleep(3)
        rec.zones["Zone2"].update()
        # print("The receiver final input is: ", rec.zones["Zone2"].input_func)

    def input_down():
        input_change(0)

    def input_up():
        input_change(1)

    while True:

        # Input control
        input_rotor.when_rotated_clockwise = input_up
        input_rotor.when_rotated_counter_clockwise = input_down

        # Volume control
        volume_rotor.when_rotated_clockwise = volume_up
        volume_rotor.when_rotated_counter_clockwise = volume_down

        # Mute Button
        mute_button.when_pressed = press_mute

        pause()


if __name__ == "__main__":
    pi_dial()

import asyncio

# from typing import list
from time import sleep
import time
import denonavr
from RPLCD.i2c import CharLCD
from signal import pause
from gpiozero import Button, RotaryEncoder


# Address of backpack
i2c_address = 0x27

# Initialize display
lcd = CharLCD("PCF8574", 0x27)

# Connect to the Denon receiver
zones = {"Zone2": "Paul Office"}
rec = denonavr.DenonAVR("192.168.1.119", name="Main Zone", add_zones=zones)
rec.update()
rec.zones["Zone2"].update()
rec_volume = float(rec.zones["Zone2"].volume)

# Zone 2 information
zone2_volume = rec.zones["Zone2"].volume
zone2_input = rec.zones["Zone2"].input_func
zone2_input_list = rec.zones["Zone2"].input_func_list

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


def main():

    loop = asyncio.get_event_loop()

    vol_up = loop.create_task(volume_up())
    vol_down = loop.create_task(volume_down())
    mute = loop.create_task(press_mute())
    change_input = loop.create_task(input_change())

    avr_status = loop.create_task(setup_avr())

    all_tasks = [vol_up, vol_down, mute, change_input, avr_status]
    loop.run_forever(all_tasks)

    loop = asyncio.get_event_loop()

    #  loop.run()


async def setup_avr():

    await rec.async_setup()
    await rec.async_update()

    print("Async method volume is: ", rec.volume)


async def volume_up():
    await volume_rotor.when_rotated_clockwise
    await rec.volume_up


async def volume_down():
    await volume_rotor.when_rotated_counter_clockwise
    await rec.volume_down


async def press_mute():
    await rec.async_setup()

    if rec.zones["Zone2"].muted is True:
        await rec.async_mute_off()
    else:
        await rec.async_mute_on()


async def input_change(inp_dir):
    pass


async def input_down():
    pass


async def input_up():
    pass

import asyncio

# from typing import list
import denonavr
from gpiozero import Button, RotaryEncoder


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
input_rotor = RotaryEncoder(19, 26, wrap=True, max_steps=24)
# print("rotor step starts at: ", input_rotor.max_steps)
input_rotor.steps = len(zone2_input_list)
# print(zone2_input, type(zone2_input), zone2_input_list.index(zone2_input))

# See README for how you can make the power button work automagically
# See also: https://embeddedpi.com/documentation/gpio/mypi-industrial-raspberry-pi-psu-shutdown-gpio-line
# power_button = Button(21)


#async def setup_avr():
#    await rec.async_setup()
#    await rec.async_update()
#    print("Async method volume is: ", rec.volume)


# async def volume_control():
async def volume_up():
    louder_steps = volume_rotor.steps
    rec.zones["Zone2"].volume_up()
    rec.zones["Zone2"].update()
    await asyncio.sleep(0.1)

    # print("Turned it up this much: ", louder_steps)


async def volume_down():
    softer_steps = volume_rotor.steps
    await rec.zones["Zone2"].volume_down()
    await rec.zones["Zone2"].update()
    await asyncio.sleep(0.1)
    # print("Turned it down this much: ", softer_steps)


async def rotor_control():
    volume_rotor.when_rotated_clockwise = volume_up
    volume_rotor.when_rotated_counter_clockwise = volume_down


async def main():
    # setup = asyncio.create_task(setup_avr())
    # volume_up_task = asyncio.create_task(volume_up())
    # volume_down_task = asyncio.create_task(volume_down())
    rotor_task = asyncio.create_task(rotor_control())

    await asyncio.gather(rotor_task)


while True:
    asyncio.run(main())

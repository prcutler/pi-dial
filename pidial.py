import asyncio
import denonavr
from gpiozero import Button, RotaryEncoder


bad_input_list = [0, 2, 4]

zones = {"Zone2": "Paul Office"}
rec = denonavr.DenonAVR("192.168.1.119", name="Main Zone", add_zones=zones)

volume_rotor = RotaryEncoder(5, 6, wrap=False, max_steps=60)
mute_button = Button(13)
input_rotor = RotaryEncoder(19, 26, wrap=True, max_steps=24)


async def setup():
    await rec.async_setup()
    await rec.zones["Zone2"].async_update()
    await rec.zones["Zone2"].async_mute(False)
    await rec.zones["Zone2"].async_set_volume(-40.0)
    await rec.zones["Zone2"].async_update()
    volume_rotor.steps = float(rec.zones["Zone2"].volume)
    input_rotor.steps = len(rec.zones["Zone2"].input_func_list)


async def volume_up():
    await rec.zones["Zone2"].async_volume_up()
    await rec.zones["Zone2"].async_update()


async def volume_down():
    await rec.zones["Zone2"].async_volume_down()
    await rec.zones["Zone2"].async_update()


async def press_mute():
    if rec.zones["Zone2"].muted:
        await rec.zones["Zone2"].async_mute(False)
    else:
        await rec.zones["Zone2"].async_mute(True)
    await rec.zones["Zone2"].async_update()


async def input_change(inp_dir):
    zone2_input_list = rec.zones["Zone2"].input_func_list
    current_input = rec.zones["Zone2"].input_func
    curr_pos = zone2_input_list.index(current_input)

    if inp_dir == 1:
        new_index = 0 if curr_pos == 12 else curr_pos + 1
        while new_index in bad_input_list:
            new_index += 1
            if new_index >= 13:
                new_index = 0
    else:
        new_index = 12 if curr_pos == 0 else curr_pos - 1
        while new_index in bad_input_list:
            new_index -= 1
            if new_index <= 0:
                new_index = 12

    await rec.zones["Zone2"].async_set_input_func(zone2_input_list[new_index])
    await asyncio.sleep(0.5)
    await rec.zones["Zone2"].async_update()


async def main():
    await setup()

    loop = asyncio.get_event_loop()

    def make_callback(coro_func, *args):
        def callback():
            asyncio.run_coroutine_threadsafe(coro_func(*args), loop)
        return callback

    volume_rotor.when_rotated_clockwise = make_callback(volume_up)
    volume_rotor.when_rotated_counter_clockwise = make_callback(volume_down)
    mute_button.when_pressed = make_callback(press_mute)
    input_rotor.when_rotated_clockwise = make_callback(input_change, 1)
    input_rotor.when_rotated_counter_clockwise = make_callback(input_change, 0)

    # Keep the event loop running while gpiozero callbacks dispatch work onto it
    stop = asyncio.Event()
    await stop.wait()


if __name__ == "__main__":
    asyncio.run(main())

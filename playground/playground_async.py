import denonavr
import asyncio


d = denonavr.DenonAVR("192.168.1.119")
# d.async_setup()
# d.async_update()

print("the volume is: ", d.volume)


async def setup_avr():

    d.async_setup()
    d.async_update()
    await d.async_setup()
    await d.async_update()

    print("Async method volume is: ", d.volume)


asyncio.run(setup_avr())


d.async_setup
d.async_bass_down
d.async_bass_up
d.async_treble_down
d.async_treble_up
d.async_mute
d.async_unmute
d.async_volume_down
d.async_volume_up
d.async_set_volume(50)
d.async_set_volume(50, True)
d.async_set_volume(50, False)

d.async_power_off
d.async_power_on

d.async_set_input_func

d.async

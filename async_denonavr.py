import denonavr
import asyncio


d = denonavr.DenonAVR("192.168.1.119")
# d.async_setup()
# d.async_update()

print("the volume is: ", d.volume)


async def main():
    async def setup_avr():

        await d.async_setup()
        await d.async_update()

        print("Async method volume is: ", d.volume)


# asyncio.run(setup_avr())

if __name__ == "__main__":
    asyncio.run(main)

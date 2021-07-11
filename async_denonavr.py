import denonavr

d = denonavr.DenonAVR("192.168.1.119")
d.async_setup()
d.async_update()

print(d.volume)

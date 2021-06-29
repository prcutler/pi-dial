import denonavr


# Set Denon AVR stats
zones = {"Zone2": "Zone 2"}
rec = denonavr.DenonAVR("192.168.1.119", name="Main Zone", add_zones=zones)
# rec.async_setup()
# rec.async_update()
rec.update()
rec.zones['Zone2'].update()


# Mute Zone 2
# print(rec.zones)
print("Main Zone Volume: ", rec.volume)
print("Main Zone Power: ", rec.power)
print("Zone 2 Volume: ", rec.zones['Zone2'].volume)
print("Zone Power: ", rec.zones['Zone2'].power)
print("Main Zone Input: ", rec.input_func)
print("Zone 2 Input: ", rec.zones['Zone2'].input_func)



# rec.async_mute
# rec.async_update()
# print("Muting Main Zone")
# receiver = rec.zones['Zone2']
# print(rec.zones['Zone2'].mute, rec.zones['Zone2'].volume)
#print(rec.zones)

# rec.zones['Zone2']
# rec.async_update()
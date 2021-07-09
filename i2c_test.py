from RPi_GPIO_i2c_LCD import lcd
from time import sleep
import denonavr

## Address of backpack
i2c_address = 0x27

## Initalize display
lcdDisplay = lcd.HD44780(i2c_address)

# Set Denon AVR stats
zones = {"Zone2": "Paul Office"}
rec = denonavr.DenonAVR("192.168.1.119", name="Main Zone", add_zones=zones)
rec.update()
rec.zones["Zone2"].update()

zone2_volume = rec.zones["Zone2"].volume
zone2_input = rec.zones["Zone2"].input_func
print(zone2_volume, zone2_input)

## Set string value to buffer
lcdDisplay.set("Volume: ", zone2_volume, 1)
lcdDisplay.set("Input: ", zone2_input, 2)

sleep(1)

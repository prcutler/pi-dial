from RPi_GPIO_i2c_LCD import lcd
from time import sleep
import denonavr
from signal import pause
from time import sleep

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


def lcd_display():
    def lcd_query():
        while True:

            display_volume = "Volume: " + str(zone2_volume)
            display_input = "Input: " + str(zone2_input)

            ## Display on LCD screen:
            lcdDisplay.set(display_volume, 1)
            lcdDisplay.set(display_input, 2)

    pause()


if __name__ == "__main__":
    lcd_display()

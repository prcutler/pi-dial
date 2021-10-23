from signal import pause
from time import sleep

import denonavr
from RPi_GPIO_i2c_LCD import lcd

## Address of backpack
i2c_address = 0x27

## Initalize display
lcdDisplay = lcd.HD44780(i2c_address)

# Set Denon AVR stats
zones = {"Zone2": "Paul Office"}
rec = denonavr.DenonAVR("192.168.1.119", name="Main Zone", add_zones=zones)
rec.update()
rec.zones["Zone2"].update()

# print(zone2_volume, zone2_input)


def lcd_query():
    # Text to display on the LCD
    rec.zones["Zone2"].update()

    zone2_volume = rec.zones["Zone2"].volume
    zone2_input = rec.zones["Zone2"].input_func

    # Clear Display
    lcd.clear()

    display_volume = "Volume: " + str(zone2_volume)
    display_input = "Input: " + str(zone2_input)
    print("Zone2: volume ", zone2_volume, "Input: ", zone2_input)

    ## Order text appears on the LCD:
    lcdDisplay.set(display_volume, 1)
    lcdDisplay.set(display_input, 2)


def lcd_display():

    while True:

        rec.zones["Zone2"].update()

        sleep(5)
        lcd_query()


if __name__ == "__main__":
    lcd_display()

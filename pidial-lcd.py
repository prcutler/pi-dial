from signal import pause
from time import sleep
import denonavr
from RPLCD.i2c import CharLCD

## Address of backpack
i2c_address = 0x27

## Initalize display
lcd = CharLCD("PCF8574", 0x27)

# Connect to the Denon receiver
zones = {"Zone2": "Paul Office"}
rec = denonavr.DenonAVR("192.168.1.119", name="Main Zone", add_zones=zones)
rec.update()
rec.zones["Zone2"].update()

# Method to display input and volume on LCD
def lcd_query():
    # Poll the receiver
    rec.zones["Zone2"].update()

    # Get the current volume and input
    zone2_volume = rec.zones["Zone2"].volume
    zone2_input = rec.zones["Zone2"].input_func
    zone2_mute = rec.zones["Zone2"].muted

    if zone2_mute == True:
        display_volume = "Mute Engaged"
        display_input = "Input: " + str(zone2_input)

        # Display Mute and Input on LCD
        lcd.clear()
        lcd.write_string(display_input)
        lcd.crlf()
        lcd.write_string(display_volume)

    else:
        display_volume = "Volume: " + str(zone2_volume)
        display_input = "Input: " + str(zone2_input)

        ## Write to the LCD (first clear it), write line one, line break, write line two
        lcd.clear()
        lcd.write_string(display_input)
        lcd.crlf()
        lcd.write_string(display_volume)


def lcd_display():

    while True:

        zone2_mute = rec.zones["Zone2"].muted

        if zone2_mute == True:
            lcd.clear()
            sleep(1)
            lcd_query()

        else:
            lcd_query()
            sleep(0.5)


if __name__ == "__main__":
    lcd_display()

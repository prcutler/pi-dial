from time import sleep
import time
import denonavr
from RPLCD.i2c import CharLCD
from signal import pause

## Address of backpack
i2c_address = 0x27

## Initalize display
lcd = CharLCD("PCF8574", 0x27)

# Connect to the Denon receiver
zones = {"Zone2": "Paul Office"}
rec = denonavr.DenonAVR("192.168.1.119", name="Main Zone", add_zones=zones)
rec.update()
rec.zones["Zone2"].update()

# Mute Display
framebuffer = [
    "",
    "",
]


def lcd_display():
    def write_muted(lcd, framebuffer, num_cols):
        """Write the framebuffer out to the specified LCD."""
        lcd.home()
        for row in framebuffer:
            lcd.write_string(row.ljust(num_cols)[:num_cols])
            lcd.write_string("\r\n")

    write_muted(lcd, framebuffer, 16)

    mute_string = "Mute Engaged"

    def mute_loop(string, lcd, framebuffer, row, num_cols, delay=0.2):
        padding = " " * num_cols
        s = padding + string + padding
        for i in range(len(s) - num_cols + 1):
            framebuffer[row] = s[i : i + num_cols]
            write_muted(lcd, framebuffer, num_cols)
            time.sleep(delay)

    def muted_state():
        rec.zones["Zone2"].update()

        if rec.zones["Zone2"].muted is True:
            lcd.clear()
            print("Muting")
            mute_loop(mute_string, lcd, framebuffer, 1, 16)

        else:
            pass

    def not_muted():

        rec.zones["Zone2"].update()
        zone2_input = rec.zones["Zone2"].input_func

        if rec.zones["Zone2"].muted is False:

            lcd.clear()
            display_volume = "Volume: " + str(rec.zones["Zone2"].volume)
            display_input = "Input: " + str(zone2_input)

        else:
            pass

        ## Write to the LCD (first clear it), write line one, line break, write line two
        lcd.clear()
        lcd.write_string(display_input)
        lcd.crlf()
        lcd.write_string(display_volume)
        sleep(0.1)

    while True:
        sleep(0.1)
        muted_state()
        not_muted()


if __name__ == "__main__":
    lcd_display()

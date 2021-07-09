import RPi_I2C_driver
from time import *

mylcd = RPi_I2C_driver.lcd()

# test 2
mylcd.lcd_display_string("RPi I2C test", 1)
mylcd.lcd_display_string(" Custom chars", 2)

sleep(2)  # 2 sec delay

from RPi_GPIO_i2c_LCD import lcd
from time import sleep

## Address of backpack
i2c_address = 0x27

## Initalize display
lcdDisplay = lcd.HD44780(i2c_address)

## Set string value to buffer
lcdDisplay.set("Hello", 1)
lcdDisplay.set("World", 2)

sleep(1)

[![Project Type: Toy](https://img.shields.io/badge/project%20type-toy-blue)](https://project-types.github.io/#toy)
[![Open in Visual Studio Code](https://open.vscode.dev/badges/open-in-vscode.svg)](https://open.vscode.dev/prcutler/pi-dial)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

![pi-dial in enclosure](/img/pidial.png)

# Pi-Dial
Pi-Dial consists of two Python programs that can be used with a Raspberry Pi to control Zone 2 of a Denon audio-visual receiver (AVR).  You will also need 16x2 LCD display and two rotary encoders.  Grogu not included.  For more information you can read my series  [of blog posts ](https://paulcutler.org/tags/pi-dial/) over 2021 creating `pi-dial`.

## Features
* Control the volume of Zone 2 using a rotary encoder
* Change the input source of Zone 2 using a rotary encoder
* Mute the receiver by pushing the button on the volume rotary encoder
* Use the LCD display to show the current input, volume, and mute status
* `systemd` service files included to start the programs at boot
* 3D Printer STLs included (unfortunately, the CAD file has been lost)

## Requirements
* Raspberry Pi 2 or later
* Rotary encoder (2)
* 16x2 LCD display
* Denon audio-visual receiver (AVR)
* 3D printer (optional)
* Micro-USB extension cable (optional)
* Python 3 (Built using 3.9)
* systemd (optional)

## Installation

1. Connect the LCD display and rotary encoders to the Raspberry Pi.  Make a note of which GPIO pins you connect each one to.  Enable the [I2C interface on the Raspberry Pi ](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c) if needed and note its address.
2. Install Raspbian on your Raspberry Pi. Any Raspberry Pi should work, I am using an older Raspberry Pi 2 with ethernet as that is what I had laying around.
3. I recommend [changing the Raspberry Pi hostname](https://www.tomshardware.com/how-to/raspberry-pi-change-hostname) to something unique.
4. SSH into your Raspberry Pi or connect a keyboard and monitor.
5. Clone this repository.
6. Create a Python 3 virtual environment.
7. Install the Python 3 packages using `pip3 install -r requirements.txt`.
8.  Update both `pidial.py` and `pidial_lcd.py` to use the GPIO pins  and I2C address you noted in step 1.
9. Update the both files with the correct IP address of your Denon receiver.
10. Edit both `systemd` files with the directory location of your Python virtual environment and the two `pi-dial` programs. (You can directly call the Python interpreter from the virtual environment and it will use that virtual environment without having to activate it.)  Also edit the user to match your system.
10. Copy the systemd service files to `/etc/systemd/system/` (You will need to use `sudo`.)
11. Start the programs using `systemctl start pidial.service` and `systemctl start pidial_lcd.service`.  You will want to [enable the `systemd` service every time you turn your Pi on](https://www.linode.com/docs/guides/start-service-at-boot/).

## Notes
* On line 8 of `pidial.py` you will notice that I had to comment out three inputs on the receiver.  I have no idea why and [more information is in my blog post](https://paulcutler.org/posts/2021/09/pi-dial-part-6-when-is-a-list-not-a-list/).
* The `3d-printer` directory contains two STL files if you wish to print the enclosure.
* We had to glue the LCD screen into the enclsoure.  Your mileage may vary.
* We unfortunately lost the CAD file, so that is not included.
* The 'img' directory includes the photo above, one showing mute in action, and a photo showing the internals all wired up.
* If you want to see some atrocious Python code, you can see my brainstorming code in the `playground` directory.  I don't recommend it.

## TODO
* The code using the `denonavr` library needs to be refactored to use Python's `async`. More information [is available at the `denonavr` repository](https://github.com/ol-iver/denonavr)).
* The code needs tests.  Shame on me.
* I'm sure the code could be more Pythonic.  I'm still learning.
* Write a method to center the text on each line of the LCD display.

## Credits
* Originally inspired by the [Media Dial](https://learn.adafruit.com/media-dial/circuit-diagram) project on Adafruit by the Ruiz brothers
* The [denonavr project](https://github.com/ol-iver/denonavr) originally created for Home Assistant
* Way too many tutorials and guides on how to program rotary encoders and the LCD screen.  A special shout out to Adafruit for all of their project ideas and documentation.
* The [RPLCD](https://github.com/dbrgn/RPLCD) library, which is used to interface with the LCD screen.  This library was a last minute addition replacing a different library I was having issues with. 
* My best friend who wishes to remain nameless for designing the CAD files for the enclosure.
* Last, but not least, my wonderful wife, who fixed the list problem mentioned in the Notes above.

## How to contribute

Imposter syndrome disclaimer: I want your help. No really, I do.  I'm a hobbyist with a lot to learn about Python.

There might be a little voice inside that tells you you're not ready; that you need to do one more tutorial, or learn another framework, or write a few more blog posts before you can help me with this project.

I assure you, that's not the case.

And you don't just have to write code. You can help out by writing documentation, tests, or even by giving feedback about this work. (And yes, that includes giving feedback about the contribution guidelines.)

Thank you for contributing!

Questions?  Bugs?  Feel free to file an issue and let me know!  Thanks!
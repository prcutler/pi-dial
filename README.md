[![Project Type: Toy](https://img.shields.io/badge/project%20type-toy-blue)](https://project-types.github.io/#toy)
[![Open in Visual Studio Code](https://open.vscode.dev/badges/open-in-vscode.svg)](https://open.vscode.dev/prcutler/pi-dial)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

![pi-dial in enclosure](/img/pidial.png)

# Pi-Dial
Pi-Dial consists of two Python programs that can be used with a Raspberry Pi to control Zone 2 of a Denon audio-visual receiver (AVR).  You will also need 16x2 LCD display and two rotary encoders.  Grogu not included.

## Features
* Control the volume of Zone 2 using a rotary encoder
* Change the input source of Zone 2 using a rotary encoder
* Mute the receiver by pushing the volume rotary encoder
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

Install Raspbian on your Raspberry Pi. Any Raspberry Pi should work, I am using an older Raspberry Pi 2 with ethernet.                                                                                                                                                 


## Credits
* Originally inspired by the [Media Dial](https://learn.adafruit.com/media-dial/circuit-diagram) project on Adafruit by the Ruiz brothers
* The [denonavr project](https://github.com/ol-iver/denonavr) originally created for Home Assistant
* Way too many tutorials and guides on how to program rotary encoders and the LCD screen.  A special shout out to Adafruit for all of their project ideas and documentation.


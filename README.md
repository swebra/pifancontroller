# Pi Fan Controller
A simple, temperature-based fan controller for a Raspberry Pi.

Loosely based on the work done by Edoardo Paolo Scalafiotti found [here](https://hackernoon.com/how-to-control-a-fan-to-cool-the-cpu-of-your-raspberrypi-3313b6e7f92c), this simple python script controls a cooling fan using a BJT transistor connected via GPIO. It makes use of two temperature variables (a minimum and a maximum), allowing the user to define a temperature *range* to oscillate within, avoiding rapid on/off switching when trying to stabilize around a single value.

See [imswebra.com](https://www.imswebra.com/projects/pifancontroller/) for more information on how I personally use this script.

## Defaults
- Fan turns on when the CPU temperature reaches 60°C
- Fan turns off when the CPU temperature returns to 50°C.
- The temperature is checked every 10 seconds.
- The base pin of the transistor used to control the fan should be connected to [BCM pin 14](https://pinout.xyz/pinout/pin8_gpio14).

See the script's inline comments for more information on the user variables.

## Installation
If installing on Raspberry Pi OS Lite (previously Raspbian Lite), `gpiozero` may need to [be installed](https://gpiozero.readthedocs.io/en/stable/installing.html).

Download or clone the script and add `python3 /path/to/pifancontroller.py &` to your [`rc.local`](https://www.raspberrypi.org/documentation/linux/usage/rc-local.md) file to have the script run on boot.

## License
This work is licensed under the [MIT](https://opensource.org/licenses/MIT) license.

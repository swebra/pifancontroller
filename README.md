# Pi Fan Controller
A simple, temperature-based fan controller for a Raspberry Pi.

Loosely based on the work done by Edoardo Paolo Scalafiotti found [here](https://hackernoon.com/how-to-control-a-fan-to-cool-the-cpu-of-your-raspberrypi-3313b6e7f92c), this simple python script controls a cooling fan using a BJT transistor connected via GPIO. It makes use of two temperature variables (a minimum and a maximum), allowing the user to define a temperature *range* to oscillate within, avoiding rapid on/off switching when trying to stabilize around a single value.

See [imswebra.com](https://www.imswebra.com/projects/pifancontroller/) for more information on how I personally use this script.

## License
This work is licensed under the [MIT](https://opensource.org/licenses/MIT) license.

androidkeyboard
===============

Short script that allows to use computer's keyboard to simulate android keyboard

This script can be useful for testing keyboard navigation in android applications.


The script uses ```adb shell``` commands to emulate key press.

Currently supported keys:
* UP/DOWN/LEFT/RIGHT
* PAGE UP/PAGE DOWN
* BACKSPACE (used as back key in device)
* TAB
* ENTER
 

'q' need to be pressed to quit this mode (this script uses curses library, therefore the terminal might become messed if it doesn't quit properly, like when CTRL+C is pressed)

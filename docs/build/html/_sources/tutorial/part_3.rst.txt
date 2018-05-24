Part 3: The micro:bit code
===========================

Now to need to write the code to send to the micro:bit.
Open a text file in the project folder and type:

.. code:: python

  from microbit import *

  while True:
    if button_a.is_pressed():
      print("Button A")
      display.show("A")
      sleep(250)

    if button_b.is_pressed():
      print("Button B")
      display.show("B")
      sleep(250)

First we import the microbit library
This allows us to interface with the micro:bit

Then we say:

- Continue doing everything I am about to say forever
- If I press down the button labeled A then send the text "Button A" to the computer
- Also Show the letter "A" on the display so I know I pressed it.
- After you have sent the message to the computer, wait for a quarter of a second before continuing
- If I press down the button labeled B then send the text "Button B" to the computer
- Also Show the letter "B" on the display so I know I pressed it.
- After you have sent the message to the computer, wait for a quarter of a second before continuing

Now we want to save that file. I will call it `mb.py`.  Now we want to send it to the micro:bit. First plug the micro:bit into your computer with the microusb cabel then type

.. code:: sh

  uflash mb.py


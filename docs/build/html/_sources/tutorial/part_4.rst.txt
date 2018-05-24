Part 4: The computers code
===========================

The next (and last) bit of code we are going to write is for the computer.
Open up a text file called 'computer.py' and write the following:

.. code:: python

  from microbitdongle import Dongle

  mb = Donlge(debug=True)  # debug shows us useful pairing info / errors

  while True:
    print(mv.recv())  # print what we recieve from the micro:bit

The first line of the code imports the microbitdongle library. This is what does the work for us.

The next line (`mb = Dongle(debug=True)`) creates a connection to the micro:bit. debug=True means that useful information will be spat out to the console.

Finally we go into a loop. Everything inside `while True:` (in this case just `print(mv.recv())`) gets ran until the program in closed. The cotents of the loop does this:

- Has the micro:bit sent me some data?
- Yes it has!
- Ok. Im now gonna `print` this data to the console
- The micro:bit sent no data?
- Im just gonna wait until it does


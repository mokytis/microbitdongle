microbitdongle
==============

About
-----

Microbitdongle allows you to communicate with a micro:bit over serial.

Installation / Usage
--------------------

To install type ``pip install microbitdongle`` into a terminal.

Here is some example code

.. code-block:: python
    :caption: example.py
    :name: example-py
    from microbitdongle import Dongle

    mb = Dongle(debug=True) # debug=False by default. Shows useful pairing information

    while True:
        data = mb.recv()
        print(data)

you can also send data to the micro:bit usin
``mb.send("display.scroll('hi')\r")``

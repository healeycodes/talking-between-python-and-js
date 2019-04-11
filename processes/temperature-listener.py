# temperature-listener.py

import sys
from subprocess import Popen, PIPE

temperatures = []  # store temperatures
sensor = Popen(['node', 'sensor.js'], stdout=PIPE)
buffer = b''
while True:

    # read sensor data one char at a time
    out = sensor.stdout.read(1)

    # after a full reading
    if out == b'\n':
        temperatures.append(float(buffer))
        print(temperatures)
        buffer = b''
    else:
        buffer += out  # append to buffer

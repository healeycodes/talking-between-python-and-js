import sys
from subprocess import Popen, PIPE

temperatures = []  # store temperatures
proc = Popen(['node', 'sensor.js'], stdout=PIPE)
while proc.poll() is None:
    out = proc.stdout.read(1)
    sys.stdout.write(out)
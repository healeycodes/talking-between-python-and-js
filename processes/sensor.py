# sensor.py

import random, time
while True:
    time.sleep(random.random() * 5)  # wait 0 to 5 seconds
    temperature = (random.random() * 20) - 5  # -5 to 15
    print(temperature, flush=True, end='')

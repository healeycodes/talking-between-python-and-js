# sensor.py
import random, time
while True:
    time.sleep(random.random() * 5)  # wait 0 to 5 seconds
    temperature = (random.random() * 20) - 5  # -5 to 15
    print(temperature, flush=True)

'''output looks like:
7.6803759247865635
11.739795706055407
8.766955952708306'''
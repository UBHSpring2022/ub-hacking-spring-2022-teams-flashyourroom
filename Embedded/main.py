import requests
import time
import board
import neopixel
import math

# Web API to grab from
# http://3.91.155.146:5000/
api_url = 'http://3.91.155.146:5000/'

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 100

ORDER = neopixel.RGB

frequency = 0

area = [
    range(0, 25),
    range(25, 50),
    range(50, 75),
    range(75, num_pixels)
]

area_led = [
    {"red":"", "green":"", "blue":"", "frequency":0.0},
    {"red":"", "green":"", "blue":"", "frequency":0.0},
    {"red":"", "green":"", "blue":"", "frequency":0.0},
    {"red":"", "green":"", "blue":"", "frequency":0.0}
]

json_ints = ["red", "green", "blue"]

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=1, auto_write=False, pixel_order=ORDER
)

def color(red, green, blue, led_region):
    for i in led_region:
        # print(i, red, green, blue)
        pixels[i] = (
            red,
            green,
            blue
            )

time_start = time.time()
previous_res = None

print("LED Controller", flush=True)
while True:

    if ((time.time() - time_start) > 1.0):
        time_start = time.time()

        response = None
        try:
            response = requests.get(api_url)
        except:
            print("NO CONNECTION!!!", flush=True)

        if (response and response != previous_res):
            json = response.json()

            for i in range(len(area_led)):
                index = str(i+1)

                alpha = float(json[index]["brightness"])
                area_led[i]["frequency"] = float(json[index]["frequency"])
                if (alpha < 0.05):
                    alpha = 0
                for key in area_led[i].keys():
                    area_led[i][key] = str(json[index][key])
                    area_led[i][key] = alpha * int(area_led[i][key])

        for i in range(len(area_led)):
                    color(area_led[i]["red"], area_led[i]["green"], area_led[i]["blue"], area[i])
        pixels.show()
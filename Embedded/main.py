import requests
import time
import board
import neopixel

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
    {"red":"", "green":"", "blue":""},
    {"red":"", "green":"", "blue":""},
]

json_ints = ["red", "green", "blue"]

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

def color(red, green, blue):
    red = int(red)
    green = int(green)
    blue = int(blue)
    for i in range(num_pixels):
        pixels[i] = (red, green, blue)

time_start = time.time()
previous_res = None

print("LED Controller")
while True:

    if ((time.time() - time_start) > 1.0):
        time_start = time.time()

        response = None
        try:
            response = requests.get(api_url)
        except:
            pass

        if (response and response != previous_res):
            json = response.json()

            if ("red" in json.keys()):
                pixels.brightness = json["brightness"]

                for i in range(area_led[key]):
                    index = str(i+1)
                    for key in json[index]:
                        area_led[key] = str(json[key])
            else:
                for i in range(len(area_led[key])):
                    pixels.brightness = json["1"]["brightness"]

                    index = str(i+1)
                    for key in json[index]:
                        area_led[i][key]# = str(json[index][key])

            color(area_led["red"], area_led["green"], area_led["blue"])
            pixels.show()

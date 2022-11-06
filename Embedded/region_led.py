class Region_LED:
    r = 0
    g = 0
    b = 0
    a = 1.0
    effect = 0
  
    def __init__(self, pixels, range, max_led):
        self.pixels = pixels
        self.range = range
        self.max_led = max_led
        self.effect_var = 0

    def setStaticColor(self, tup):
        self.r = tup[0]
        self.g = tup[1]
        self.b = tup[2]

    def setEffect(self, ef):
        self.effect = ef
        self.effect_var = 0

    def static(self, i):
        return (
            self.r * self.a, 
            self.g * self.a, 
            self.b * self.a
            )

    def cycle(self, i):

        return

    def random(self, i):
        return (
            (self.r) % 255
        )

    effect_lists = [
        static,
        cycle,
        random
    ]

    def color(self, i):
        self.effect_var += 1
        return self.effect_lists[self.effect](i)

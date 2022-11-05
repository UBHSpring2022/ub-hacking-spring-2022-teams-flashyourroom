#include <Arduino.h>
#include <FastLED.h>

#define NUM_LEDS 100
#define DATA_PIN 3

// Define the array of leds
CRGB leds[NUM_LEDS];

void setup() { 
	Serial.begin(57600);
	Serial.println("resetting");
	LEDS.addLeds<WS2811,DATA_PIN,RGB>(leds,NUM_LEDS);
	LEDS.setBrightness(84);
}

void loop() { 
	static uint8_t hue = 0;
	Serial.print("x");
	// First slide the led in one direction
	for(int i = 0; i < NUM_LEDS; i++) {
		// Set the i'th led to red 
		leds[i] = CHSV(hue, 255, 255);
		// Show the leds
		// now that we've shown the leds, reset the i'th led to black
		// leds[i] = CRGB::Black;
		// Wait a little bit before we loop around and do it again
	}
	FastLED.show(); 
	hue++;
	delay(10);
	Serial.print("x");
}
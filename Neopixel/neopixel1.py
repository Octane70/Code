# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel


# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 12

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False,
                           pixel_order=ORDER)

#Colors
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)

try:
    while True:
        pixels[0] = (RED)
        pixels[1] = (BLUE)
        pixels[2] = (RED)
        pixels[3] = (RED)
        pixels[4] = (BLUE)
        pixels[5] = (RED)
        pixels[6] = (RED)
        pixels[7] = (BLUE)
        pixels[8] = (RED)
        pixels[9] = (RED)
        pixels[10] = (BLUE)
        pixels[11] = (RED)
        pixels.show()
        time.sleep(1)

        pixels.fill(OFF)
        pixels.show()
        time.sleep(1)

        pixels[0] = (BLUE)
        pixels[1] = (RED)
        pixels[2] = (BLUE)
        pixels[3] = (BLUE)
        pixels[4] = (RED)
        pixels[5] = (BLUE)
        pixels[6] = (BLUE)
        pixels[7] = (RED)
        pixels[8] = (BLUE)
        pixels[9] = (BLUE)
        pixels[10] = (RED)
        pixels[11] = (BLUE)
        pixels.show()
        time.sleep(1)

        pixels.fill(OFF)
        pixels.show()
        time.sleep(1)


# If a keyboard interrupt occurs (ctrl + c), the GPIO is set to 0 and the program exits.
except(KeyboardInterrupt):
    print("Fan ctrl interrupted by keyboard")
    pixels.fill(OFF)
    pixels.show()


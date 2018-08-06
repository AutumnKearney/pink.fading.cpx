from adafruit_circuitplayground.express import cpx
import time 

pink = (40, 10, 1) 
turquoise = (34, 100, 100)
purple = (5, 512, 12)
pinkval = 40
off = (0, 0, 0)

#slowly dim all red neopixels with loop and variable

if pinkval > 0:
    print ("pink value is " + str(pinkval))
    cpx.pixels.fill((pinkval, 0, 0))
    pinkval = pinkval - 1
    time.sleep(0.001)
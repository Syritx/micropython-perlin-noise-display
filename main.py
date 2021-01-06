import machine
import dht
import time
import ssd1306

import noise as perlin

LED_PIN_NB = 2
led = machine.Pin(LED_PIN_NB, machine.Pin.OUT)
led.on()

elapsed_time = 0

def flash_led(is_on, iteration, delay):
    global elapsed_time    

    elapsed_time = elapsed_time + delay
    if is_on:
	led.on()
	is_on = False
    else:
	led.off()
	is_on = True

    #debugging purposes
    print('receiving data. \nRound: {i}.\nTime Elapsed: {e}'.format(i=iteration, e=elapsed_time))

    return is_on

def noise_layer(x, y, l, p, o):
    n = 0
    freq = 2
    ampl = 1

    for i in range(o):
	n = n + perlin.noise(x*freq, y*freq)
	freq = freq * l
	ampl = ampl * p

    return n	


# main
def write_noise(x_range, y_range, seed, height):
    i2c = machine.I2C(scl=machine.Pin(0), sda=machine.Pin(12))
    display = ssd1306.SSD1306_I2C(128, 64, i2c)
    display.fill(0)

    perlin.seed(seed)

    for x in range(x_range):
	for y in range(y_range):

	    h = noise_layer(x/128, y/128, 2, .5, 4)
#	    print('Height {h} at: {x}, {y}'.format(h=h, x=x, y=y))

	    if h > height:
	        print("displayed")
	        display.rect(x, y, 1, 1, 1)
	   	display.show()
    display.show()

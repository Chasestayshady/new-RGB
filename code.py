
import board
import busio
import time

import adafruit_tcs34725


##################
# *EDIT*
# Set configurable values below
# Feed name for Adafruit IO

# milliseconds to gather color data
sensor_integration_time = 150

# manually override the color sensor gain
sensor_gain = 4

# Collect this many samples each time we prompt the user
num_samples = 5

#
# End of editable config values
##################

# Create sensor object, communicating over the board's default I2C bus
i2c = busio.I2C(board.GP17, board.GP16)  # uses first I2C SCA/SCL pair on pico
sensor = adafruit_tcs34725.TCS34725(i2c)

# Change sensor gain to 1, 4, 16, or 60
sensor.gain = sensor_gain
# Change sensor integration time to values between 2.4 and 614.4 milliseconds
sensor.integration_time = sensor_integration_time

while True:
    print(sensor.color_rgb_bytes)
    r = sensor.color_rgb_bytes[0]
    g = sensor.color_rgb_bytes[1]
    b = sensor.color_rgb_bytes[2]

    time.sleep(1)
    print("Temperature: %d" % sensor.color_temperature)
    print(
        "r: %d, g: %d, b: %d"
        % (
            sensor.color_rgb_bytes[0],
            sensor.color_rgb_bytes[1],
            sensor.color_rgb_bytes[2],
        )
    )



    print(sensor.color_rgb_bytes)
    print(r,g,b)
    if r>130 and g<100 and b<100:
        print("detected color is:red")
    if r<100 and g>20 and b<100:
        print("detected color is:green")
    if r>40 and g<10 and b<10:
        print("detected color is:brown")
    if r>140 and g<100 and b<100:
        print("detected color is: orange")
    if r>80 and g<80 and b<80:
        print("detected color is: yellow")


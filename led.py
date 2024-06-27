import RPi.GPIO as GPIO
import time

# Set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)

# Set up pin 17 as an output
led_pin = 17
GPIO.setup(led_pin, GPIO.OUT)

try:
    while True:
        # Turn the LED on
        GPIO.output(led_pin, GPIO.HIGH)
        print("LED on")
        time.sleep(1)  # Wait for 1 second

        # Turn the LED off
        GPIO.output(led_pin, GPIO.LOW)
        print("LED off")
        time.sleep(1)  # Wait for 1 second

except KeyboardInterrupt:
    # Clean up GPIO on CTRL+C exit
    GPIO.cleanup()

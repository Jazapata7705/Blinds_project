import RPi.GPIO as GPIO
# Define GPIO pins for motor control
IN1 = 17
IN2 = 18
GPIO.setmode(GPIO.BCM)
# Set up GPIO pins
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
def cleanup_gpio():
    GPIO.cleanup()

cleanup_gpio()

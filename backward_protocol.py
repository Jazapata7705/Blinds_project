import RPi.GPIO as GPIO
import time

# Set GPIO numbering mode
GPIO.setmode(GPIO.BCM)

# Define GPIO pins for motor control
IN1 = 17
IN2 = 18

# Set up GPIO pins
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)

# Set up PWM for controlling motor speed
pwm_frequency = 1000  # Frequency in Hz (1 kHz)
motor_pwm = GPIO.PWM(IN2, pwm_frequency)

# Function to drive motor forward at a given speed (0-100)
def backward(speed):
    motor_pwm.start(speed)
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)

# Function to stop motor
def stop():
    motor_pwm.stop()
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)

# Perform actions
try:
    backward(10)     # Move motor forward at 50% speed
    time.sleep(2)   # Move forward for 2 seconds

    stop()          # Stop motor


except KeyboardInterrupt:
    stop()          # Stop motor on keyboard interrupt

finally:
    GPIO.cleanup()  # Clean up GPIO pins

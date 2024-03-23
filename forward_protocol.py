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
motor_pwm = GPIO.PWM(IN1, pwm_frequency)

# Function to drive motor forward at a given speed (0-100)
def forward(speed):
    motor_pwm.start(speed)
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)

# Function to stop motor
def stop():
    motor_pwm.stop()
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)

# Perform actions
forward(10)     # Move motor forward at 50% speed

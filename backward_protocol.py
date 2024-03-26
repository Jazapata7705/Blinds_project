import RPi.GPIO as GPIO
import time
import atexit



# Define GPIO pins for motor control
IN1 = 17
IN2 = 18
GPIO.setmode(GPIO.BCM)
# Set up GPIO pins
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)

GPIO.output(IN1, GPIO.LOW)
GPIO.output(IN2, GPIO.LOW)
# Set up PWM for controlling motor speed
pwm_frequency = 500  # Frequency in Hz (.5 kHz)
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

if __name__ == '__main__':
    backward(20)
    while True:
        time.sleep(.5)

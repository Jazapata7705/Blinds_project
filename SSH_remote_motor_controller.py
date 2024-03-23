#The goal of this script is to use scripts from the pi and run them from the computer
import paramiko
import time


def test_ssh_connection(host, port, username, password_or_key):
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(host, port, username, password_or_key)
        print("SSH Connection successful!")
    except Exception as e:
        print(f"SSH Connection failed: {e}")
    finally:
        ssh_client.close()



# Replace these values with your actual details
host = "10.230.18.215"
port = 22
username = "jazapata7705"
password_or_key = "Galac7ic"

# Connect to Raspberry Pi
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Replace with the GPIO pin number you want to control --------------------------------------------------------------------------
gpio_pin1 = 17
gpio_pin2 = 18

#define speed/ other values for motor controller
pwm_frequency = 1000




try:
    #connect the pi to the computer through secure shell 
    ssh_client.connect(host, port, username, password_or_key)
    print('connected to pi')



finally:
    ssh_client.close()
    print("SSH connection terminated")


#The goal of this script is to use scripts from the pi and run them from the computer
import paramiko
import tkinter as tk
import socket
from zeroconf import ServiceBrowser,Zeroconf
import time




#tries to enter a ssh connection to determine if the function is working properly
def test_ssh_connection(host, port, username, password_or_key):
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(ssh_host, ssh_port, ssh_username, ssh_password_or_key)
        print("SSH Connection successful!")
    except Exception as e:
        print(f"SSH Connection failed: {e}")
    finally:
        print('terminating connection test')
        ssh_client.close()
        
# SSH command function to execute functions remotely through pi terminal
def ssh_command(command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ssh_host, port=ssh_port, username=ssh_username, password=ssh_password_or_key)
    client.exec_command(command)
    client.close()

#function to send ssh command to run python script/ protocols
def run_python_script(script_path):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ssh_host, port=ssh_port, username=ssh_username, password=ssh_password_or_key)

    
    client.exec_command(f'nohup python3 {script_path} > /dev/null 2>&1 &')
    
    client.close()

def terminate_remote_python_script(script_path):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ssh_host, port=ssh_port, username=ssh_username, password=ssh_password_or_key)

    # Execute the command to terminate the Python script
    command = f'pkill -f "{script_path}"'
    stdin, stdout, stderr = client.exec_command(command)
    output = stdout.readlines()
    client.close()
    return output

# Replace these values with your actual details
ssh_host = "10.231.158.54" #currently have to replace if IP_address changes
ssh_port = 22
ssh_username = "jazapata7705"
ssh_password_or_key = "Galac7ic"


# Connect to Raspberry Pi
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Replace with the GPIO pin number you want to control --------------------------------------------------------------------------
gpio_pin1 = 17
gpio_pin2 = 18


#define speed/ other values for motor controller
pwm_frequency = 1000
path_to_repository = '/home/jazapata7705/Blinds_project'


#Run a gui with two buttons to control the pi
#test_ssh_connection(ssh_host, ssh_port, ssh_username, ssh_password_or_key)



pressed = False
def button1_pressed(event):
    print("Button 1 Pressed")
    run_python_script('/home/jazapata7705/Blinds_project/forward_protocol.py')

def button2_pressed(event):
    print("Button 2 Pressed")
    run_python_script('/home/jazapata7705/Blinds_project/backward_protocol.py')
def button1_released(event):
    print("Button 1 Released")
    ssh_command('pkill -f "python"')
    run_python_script('/home/jazapata7705/Blinds_project/GPIO_cleanup.py')
def button2_released(event):
    print("Button 2 Released")
    ssh_command('pkill -f "python"')
    run_python_script('/home/jazapata7705/Blinds_project/GPIO_cleanup.py')


# Create the main window
root = tk.Tk()
root.title("Button Press Detection")

# Create and add buttons to the window
button1 = tk.Button(root, text="Button 1")
button1.pack()

button2 = tk.Button(root, text="Button 2")
button2.pack()

# Bind events to buttons
button1.bind("<ButtonPress-1>", button1_pressed)
button1.bind("<ButtonRelease-1>", button1_released)

button2.bind("<ButtonPress-1>", button2_pressed)
button2.bind("<ButtonRelease-1>", button2_released)


# Run the Tkinter event loop
root.mainloop()



try:
  
    #test_ssh_connection(ssh_host,ssh_port,ssh_username,ssh_password_or_key)
    
    run_python_script('/home/jazapata7705/Blinds_project/GPIO_cleanup.py')
    print("cleanup completed")
    #IT WORKKSKSKSKSKSKSKS

    #now i need to figure out  a way to consistently connect and not have to reset the ip connection
    #terminate_remote_python_script('/home/jazapata7705/Blinds_project/forward_protocol.py')

    
finally:
    ssh_client.close()
    print("SSH connection terminated")


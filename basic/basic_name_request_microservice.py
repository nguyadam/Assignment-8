import os
import time

MESSAGE_FILE = '../message_queue.txt'

def basic_name_request():
    name = "John Doe"
    return name

def send_message(service_name, message):
    with open(MESSAGE_FILE, 'a') as f:
        f.write(f"{service_name}|{message}\n")

def main():
    request_generated = False  # Variable to track whether request is generated
    while not request_generated:  # Loop until request is generated
        name = basic_name_request()
        send_message("Basic Name Request Microservice", f"Requested basic name: {name}")
        print(f"Requested basic name: {name}")
        request_generated = True  # Set flag to True after generating request
        time.sleep(5)
if __name__ == "__main__":
    main()

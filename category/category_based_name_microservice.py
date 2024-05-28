import random
import os
import time

MESSAGE_FILE = '../message_queue.txt'
NAMES = ["Alice", "Bob", "Charlie", "Dana", "Eve"]

def generate_name():
    name = random.choice(NAMES)
    return name

def send_message(service_name, message):
    with open(MESSAGE_FILE, 'a') as f:
        f.write(f"{service_name}|{message}\n")

def main():
    request_generated = False  # Variable to track whether request is generated
    while not request_generated:  # Loop until request is generated
        name = generate_name()
        send_message("Category-Based Name Microservice", f"Generated name: {name}")
        print(f"Generated name: {name}")
        request_generated = True  # Set flag to True after generating request
        time.sleep(5)

if __name__ == "__main__":
    main()

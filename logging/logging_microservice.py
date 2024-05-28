import os
import time
from datetime import datetime

LOG_FILE = 'log.txt'
MESSAGE_FILE = '../message_queue.txt'

def log_request(service_name, request_data):
    with open(LOG_FILE, 'a') as f:
        log_entry = f"{datetime.now()} - {service_name}: {request_data}\n"
        f.write(log_entry)

def read_messages():
    if os.path.exists(MESSAGE_FILE):
        with open(MESSAGE_FILE, 'r') as f:
            messages = f.readlines()
        with open(MESSAGE_FILE, 'w') as f:
            f.write('')
        return messages
    return []

def process_messages():
    while True:
        messages = read_messages()
        for message in messages:
            service_name, request_data = message.strip().split('|', 1)
            log_request(service_name, request_data)
        time.sleep(1)

def fetch_logs():
    if not os.path.exists(LOG_FILE):
        print("No logs available.")
        return
    
    with open(LOG_FILE, 'r') as f:
        logs = f.readlines()
    
    for log in logs:
        print(log.strip())

def clear_logs():
    with open(LOG_FILE, 'w') as f:
        f.write('')
    print("Logs cleared.")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Logging Microservice')
    parser.add_argument('--fetch-logs', action='store_true', help='Fetch and print all logs')
    parser.add_argument('--clear-logs', action='store_true', help='Clear all logs')

    args = parser.parse_args()

    if args.fetch_logs:
        fetch_logs()
    elif args.clear_logs:
        clear_logs()
    else:
        print("Logging microservice is running. Use --fetch-logs to fetch logs or --clear-logs to clear logs.")
        process_messages()

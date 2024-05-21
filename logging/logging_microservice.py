import os
from datetime import datetime

LOG_FILE = 'log.txt'

def log_request(service_name, request_data):
    with open(LOG_FILE, 'a') as f:
        log_entry = f"{datetime.now()} - {service_name}: {request_data}\n"
        f.write(log_entry)

def read_logs():
    if not os.path.exists(LOG_FILE):
        return "No logs available."
    
    with open(LOG_FILE, 'r') as f:
        return f.readlines()

def fetch_logs():
    logs = read_logs()
    for log in logs:
        print(log.strip())

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Logging Microservice')
    parser.add_argument('--fetch-logs', action='store_true', help='Fetch and print all logs')

    args = parser.parse_args()

    if args.fetch_logs:
        fetch_logs()
    else:
        print("Logging microservice is running. Use --fetch-logs to fetch logs.")

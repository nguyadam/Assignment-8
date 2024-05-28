To compile from the root directory: 
python compile_all.py

To start logging service:
python -m logging.logging_microservice

To fetch logs:
python -m logging.logging_microservice --fetch-logs

To clear logs:
python -m logging.logging_microservice --clear-logs

Example request from microservice:
import sys
import os

# Add the parent directory to the system path to enable module import
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from logging.logging_microservice import log_request

def basic_name_request():
    name = "John Doe"
    log_request("Basic Name Request Microservice", f"Requested basic name: {name}")
    return name

# Example request, just to previous what you are getting from the microservice
if __name__ == "__main__":
    print(basic_name_request())
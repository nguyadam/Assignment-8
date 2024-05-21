import sys
import os

# Add the parent directory to the system path to enable module import
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from logging.logging_microservice import log_request

def basic_name_request():
    name = "John Doe"
    log_request("Basic Name Request Microservice", f"Requested basic name: {name}")
    return name

# Example request
if __name__ == "__main__":
    print(basic_name_request())
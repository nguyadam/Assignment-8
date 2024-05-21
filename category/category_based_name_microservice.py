import random
import sys
import os

# Add the parent directory to the system path to enable module import
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from logging.logging_microservice import log_request

NAMES = ["Alice", "Bob", "Charlie", "Dana", "Eve"]

def generate_name():
    name = random.choice(NAMES)
    log_request("Category-Based Name Microservice", f"Generated name: {name}")
    return name

# Example request
if __name__ == "__main__":
    print(generate_name())
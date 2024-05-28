To compile from the root directory: 
python compile_all.py

**Create an empty 'log.txt' and a 'message_queue.txt' file**

To setup requests in your program, have this function:
def send_message(service_name, message):
    with open(MESSAGE_FILE, 'a') as f:
        f.write(f"{service_name}|{message}\n")

This would be the example call for send_message:

send_message("Request Name", f"Request message")
"Request Name" and "Request message" can be changed to your liking

To setup directories to run correctly(as modules):
-Have your programs in a folder to your naming, we'll describe this example folder as "example"
-In your example folder, also have an empty python file named "__init__"

To start logging service(Make sure its in its own open terminal, the terminal will not receive more input)
**Start before requests are sent**
python -m logging.logging_microservice

To send your request in a terminal, open your terminal with the root directory containing your "example" folder,
log.txt, and message_queue.txt
**Assuming your microservice is named "example_microservice"**
python -m example.example_microservice

The request above will print in log.txt:
[TIME] - Request Name: Request message

To fetch logs:
python -m logging.logging_microservice --fetch-logs

To clear logs:
python -m logging.logging_microservice --clear-logs



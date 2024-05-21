# Assignment-8

**You can request data from the program by first starting the log call:**
python -m logging.logging_microservice

**The program will then tell us its beginning to log**
**From here you can now start requesting through the microservices**
python -m category.category_based_name_microservice
python -m basic.basic_name_request_microservice

**This information will get logged in the 'log.txt' file which can be viewed externally through the current working directory**
**If we want to receive data from the microservice, we can write the following call which will fetch the logs created from each request made by the other microservices**
python -m logging.logging_microservice --fetch-logs
![image](https://github.com/nguyadam/Assignment-8/assets/147447331/94613766-fa8a-4358-85f7-ccfa39aa00a0)

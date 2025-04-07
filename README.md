# de-syntio-task-1
Task 1 (Containerization) for Syntio; Data Engineer role application

Project installation steps:

1. Clone the repository
$ git clone https://github.com/StjepanVU/de-syntio-task-1.git

2. Enter the project folder
$ cd de-syntio-task-1

3. Run Docker compose command
$ docker-compose up

4. Test functionality (Postman collection available in the project folder)
**POST** http://localhost:5000/receiver/message
body:
{
    "message" : "Lorem ipsum!"
}

**POST** http://localhost:5001/storage/store
body:
{
  "msg": "asdadas",
  "dateTimeSent": "2025-04-07T15:44:27.832538"
}

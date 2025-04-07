# de-syntio-task-1

**Task 1 (Containerization)** for Syntio – Data Engineer role application - Stjepan Milicic

## 🚀 Project Installation Steps (bash)

1. Clone the repository:

    ```bash
    git clone https://github.com/StjepanVU/de-syntio-task-1.git
    ```

---

2. Enter the project folder:

    ```bash
    cd de-syntio-task-1
    ```

---

3. Run the Docker Compose command:

    ```bash
    docker-compose up -d
    ```

---

4. Test functionality (Postman : "Syntio - Containerization - Task 1.postman_collection"):
    
    Stored JSON data is contained in **`de-syntio-task-1/storage/stored_json`** folder locally.

    **POST** `http://localhost:5000/receiver/message` (reciver server endpoint):
    ```json
    {
      "message": "Lorem ipsum!"
    }
    ```

    **POST** `http://localhost:5001/storage/store` (storage server endpoint):
    ```json
    {
      "msg": "Lorem ipsum!",
      "dateTimeSent": "2025-04-07T15:44:27.832538"
    }
    ```

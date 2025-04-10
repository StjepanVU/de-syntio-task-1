# de-syntio-task-1

**Task 1 (Containerization)** for Syntio – Data Engineer role application - Stjepan Milicic

## 🚀 Project Installation Steps (bash)

1. Clone the repository:

    ```bash
    git clone https://github.com/StjepanVU/de-syntio-task-1.git
    ```


2. Enter the project folder:

    ```bash
    cd de-syntio-task-1
    ```

3. Start Docker Desktop:

    ```bash
    docker desktop start
    ```

4. Run the Docker Compose command:

    ```bash
    docker-compose up -d
    ``` 
       
---
## 🔬 Tests
- Stored JSON data is contained in **`de-syntio-task-1/stored_json`** folder locally.
- Configurable second (storage) server endpoint is referenced in the "docker-compose.yml" variable as "STORE_API_URL" environment variable.
**POST** /receiver/message    

cURL:
```bash
curl --location 'http://localhost:5000/receiver/message' \
-H 'Content-Type: application/json' \
--data '{
    "message" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
}'
```

http://localhost:5000/receiver/message (reciver server endpoint):


```json
{
  "message": "Lorem ipsum!"
}
```
http-**200**
```json
{
"filename": "msg-Ti8AOOXu.json",
"status": "success",
"status_code": 200
}
```
--- 

**POST** /storage/store

```bash
curl --location 'http://localhost:5001/storage/store' \
-H 'Content-Type: application/json' \
--data '{
  "msg": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
  "dateTimeSent": "2025-04-07T15:44:27.832538"
}'
```

http://localhost:5001/storage/store (storage server endpoint):
```json
{
  "msg": "Lorem ipsum!",
  "dateTimeSent": "2025-04-07T15:44:27.832538"
}
```
 http-**200**
```json
{
    "filename": "msg-O4oRk57q.json",
    "status": "success"
    }
   ```

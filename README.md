# Note Taking Application API - Using python HTTP.Server

## Overview of Application

This application is a simple note-taking RESTful API that uses CRUD operations. It uses the Python language server to handle HTTP requests that allow the user to create, receive, update, and delete requests. It uses the Python `http.server` module. For the database, it uses MySQL to store and preserve data while using sql queries to make operations.

## Tools and Technology Used
- Programming Language: Python 
- Database: MySQL 
- Version Control: Git 
- Containerization: Docker 
- API Testing: Postman 

## Required knowledge
- Basic knowledge of Python programming 
- Understanding of RESTful API principles 
- Familiarity with SQL and relational databases 
- Basic understanding of Docker and containerization 
- Git installed and configured for version control

## Getting Started

1. Clone the repository using the command in cmd
```bash
git clone https://github.com/KabeerH/Note-TakingAPI
```
2. Change to the directory where you have cloned the project
```bash
cd directory
```
3. To build the project using docker
```bash 
docker-compose up --build
```
4. To start the project if not started
```bash 
docker-compose up 
```
5. To Stop the application and delete the container
```bash
docker-compose down
```

Once the application is started, you can go to http://localhost:8000/notes to access the API.

## API METHODS Functions

This API provides the following endpoints:

### GET /notes

This endpoint retrieves all notes from the database.

- Method: `GET`
- URL: `/notes`

**Usage with Postman:**
1. Set the HTTP method to `GET`.
2. Enter the request URL as `http://localhost:8000/notes`.
3. Click on `Send` to make the request.

![image](https://github.com/KabeerH/Note-TakingAPI/assets/122492914/fde7e632-b1c7-449a-9503-56dd3b29ef9b)


### POST /notes

This endpoint creates a new note in the database.

- Method: `POST`
- URL: `/notes`
- Request Body: A JSON object containing 'title' and 'content'.

**Usage with Postman:**
1. Set the HTTP method to `POST`.
2. Enter the request URL as `http://localhost:8000/notes`.
3. Click on `Body`, then select `raw` and `JSON`.
4. In the text field, enter your note in the following format: `{"title": "ok", "content": "K"}`.
5. Click on `Send` to make the request.

![image](https://github.com/KabeerH/Note-TakingAPI/assets/122492914/c124805a-34ee-42be-8960-01dc721104d1)


### PUT /notes

This endpoint updates an existing note in the database.

- Method: `PUT`
- URL: `/notes`
- Request Body: A JSON object containing 'id', 'title', and 'content'.

**Usage with Postman:**
1. Set the HTTP method to `PUT`.
2. Enter the request URL as `http://localhost:8000/notes`.
3. Click on `Body`, then select `raw` and `JSON`.
4. In the text field, enter your note in the following format: `{"id": 1, "content": "changed-once", "title": "changed-again"}`.
5. Click on `Send` to make the request.

![image](https://github.com/KabeerH/Note-TakingAPI/assets/122492914/0b0ca131-1b77-411a-b992-00c7acbdf232)


### DELETE /notes

This endpoint deletes a note from the database.

- Method: `DELETE`
- URL: `/notes`
- Request Body: A JSON object containing 'id'.

**Usage with Postman:**
1. Set the HTTP method to `DELETE`.
2. Enter the request URL as `http://localhost:8000/notes`.
3. Click on `Body`, then select `raw` and `JSON`.
4. In the text field, enter the id of the note you want to delete in the following format: `{"id": 2}`.
5. Click on `Send` to make the request.

![image](https://github.com/KabeerH/Note-TakingAPI/assets/122492914/a687b430-bf37-4b80-ac24-5257e8d1a309)

## Additional Tips
When running this appliccation replace values `DB_HOST`, `DB_USER`, `DB_PASSWORD` and `DB_DATABASE` with your own credentials or make a `.env` file and copy/paste the following into that file:
```bash
DB_HOST=
DB_USER=
DB_PASSWORD=
DB_DATABASE=
```
then set your credentials.



## Contributors 

- Kabeer Harjani | https://github.com/KabeerH

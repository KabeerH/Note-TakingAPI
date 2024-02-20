# Note Taking Application API - Using python HTTP.Server

## Overview of Application

This application is a simple note-taking RESTful API that uses CRUD operations. It uses the python language server to handle HTTP requests that allows the user to create, recieve, update and delete requests.  It uses the python -> http.server module. For the database it uses MYSQL to 
store and perserve data.

## Tools and Technology Used
• Programming Language: Python 
• Database: MySQL 
• Version Control: Git 
• Containerization: Docker 
• API Testing: Postman or curl

## Required knowledge

• Basic knowledge of Python programming 
• Understanding of RESTful API principles 
• Familiarity with SQL and relational databases 
• Basic understanding of Docker and containerization 
• Git installed and configured for version control

 ## Getting Started

1. Clone the repository using the command in cmd
\`\`\`
git clone https://github.com/KabeerH/Note-TakingAPI
\`\`\`

2. Change to the directory where you have cloned the project
 \`\`\`
cd directory
 \`\`\`

3. To build the project using docker 
\`\`\`
docker-compose up --build
 \`\`\`

4. To Stop the application and delete the container 
 \`\`\`
docker-compose down
 \`\`\`

 Once the application is started you can go to http://localhost:8000/ to access the API

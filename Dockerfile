#These set of instructions should execute when the docker container command is executed "docker-compose up --build"
FROM python:3.8-slim-buster

WORKDIR /app

ADD . /app

#install dependencies when container is started (mysql-connecctor to deal with databases) & (dotenv for security dealing with database sensitive infomation)
RUN pip install --no-cache-dir mysql-connector-python
RUN pip install python-dotenv

#launch on port 8000
EXPOSE 8000

#start the container when finish
CMD ["python", "app.py"]
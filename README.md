# Running Locally with Python
- Clone this repository
- Run the file 'fake_api_workflow.py'

# Quick explanation
All operations are stored in the 'faker' directory
- ingestion
- transformation
- data request

The file 'fake_api_workflow.py' is our main application that connects
all these operations. To see more details about the parameters please see the documentation in the file.

# Essential Parameters
You might want to change the number of rows that you want to request from the faker-api.
To do this, all you have to do is change the value of the variable 'desired_number_of_rows' inside the file 'fake_api_workflow.py'. The default value is 10000

# How to run this application using Docker
Make sure you have installed:
* docker

# Build the image using the dockerfile
Open your terminal in the directory of this project
```shell
docker build -t faker-challenge:v1 .
```

# Create a container
Now you need to create/run the container with the image
that we just built
```shell
docker run faker-challenge
```
You can also pass the flag '-it' to follow the process of the application

# Get the ID of your container
```shell
docker container ls -a
```
Search for the image of your container and copy it's ID

# Getting Data from the container
After that we need to retrieve data from the container volume
To do that
```shell
sudo docker cp <your-container-id>:/taxfix-challenge.db /taxfix-challenge.db
```
If you are using Windows, you must open your powershell in admin mode
```shell
docker cp <your-container-id>:/taxfix-challenge.db /taxfix-challenge.db
```
This command is going to copy the .db file into your current directory

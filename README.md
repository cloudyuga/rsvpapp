# RSVP App in Python
RSVP app by CloudYuga

## Steps to run the application locally
- Clone this repository
```
git clone https://github.com/cloudyuga/rsvpapp.git
```
- Install python and pip package manager
- Install python packages mentioned in `requirements.txt` file
```
pip install -r requirements.txt
```
- Install mongodb for the database.One can use mongodb as a docker container also.
```
docker container run -d -p 27017:27017 --name=mongodb mongo:3.6
```
- Run the python app locally
```
python3 rsvp.py
```
Access the application locally on port number 5000.

## Build the Docker image of the application 
- Build the Docker image from the `Dockerfile`
```
docker build -t <dockerhub_username>/rsvpapp-python:v1 .
```
- Start the frontend and backend of the application with the help of docker compose.
```
docker compose up -d
```

## Credits
Thanks to [Anand Chitipothu](https://twitter.com/anandology) for helping us with the application development. 

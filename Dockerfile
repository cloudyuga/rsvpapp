FROM teamcloudyuga/python:alpine
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN pip3 install -r requirements.txt
CMD python rsvp.py

FROM python:3.4-onbuild

COPY . /usr/src/app

RUN pip3 install -r requirements.txt


CMD python rsvptest.py

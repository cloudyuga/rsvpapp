FROM python:3.9.18-slim as build
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
	      build-essential gcc 

WORKDIR /usr/src/app
RUN python -m venv /usr/src/app/venv
ENV PATH="/usr/src/app/venv/bin:$PATH"

COPY requirements.txt .
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir  -r requirements.txt

FROM python:3.9.18-slim
RUN groupadd -g 999 python && \
    useradd -r -u 999 -g python python
RUN mkdir /usr/src/app && chown python:python /usr/src/app
WORKDIR /usr/src/app/venv
COPY --chown=python:python --from=build /usr/src/app/venv /usr/src/app/venv
COPY --chown=python:python . .
USER 999

ENV LINK http://www.meetup.com/cloudyuga/
ENV TEXT1 CloudYuga
ENV TEXT2 Garage RSVP!
ENV LOGO https://raw.githubusercontent.com/cloudyuga/rsvpapp/master/static/cloudyuga.png
ENV COMPANY CloudYuga Technology Pvt. Ltd.

ENV PATH="/usr/src/app/venv/bin:$PATH"
EXPOSE 5000
CMD ["python", "rsvp.py"]


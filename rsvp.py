import re
import os
import json
import string
import csv
import io
from flask import Flask, render_template, redirect, url_for, request,make_response
from pymongo import MongoClient
from bson.json_util import dumps
import socket
app = Flask(__name__)

MONGODB_HOST=os.environ['MONGODB_HOST']
print (MONGODB_HOST)
client = MongoClient(MONGODB_HOST, 27017)
db = client.rsvpdata

@app.route('/')
def rsvp():
	_items = db.rsvpdata.find()
	items = [item for item in _items]
	count = len(items)
	
	hostname = socket.gethostname()

	return render_template('profile.html', counter=count, hostname=hostname, items=items)
	

@app.route('/new', methods=['POST'])
def new():

	#if not re.match(r'[^@]+@[^@]+\.[^@]+', request.form['email']):
	#	return render_template('errors/403.html'), 403

	item_doc = {'name': request.form['name'], 'email': request.form['email']}
	db.rsvpdata.insert_one(item_doc)
	return redirect(url_for('rsvp'))

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)

client.close()

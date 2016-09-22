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

client = MongoClient('mongodb',27017)
db = client.rsvpdata

@app.route('/')
def rsvp():
	_items = db.rsvpdata.find()
	items = [item for item in _items]
	count = len(items)
	
	hostname = socket.gethostname()

	return render_template('profile.html',counter=count,hostname=hostname, items=items)
	

@app.route('/new', methods=['POST'])
def new():

	#if not re.match(r'[^@]+@[^@]+\.[^@]+', request.form['email']):
	#	return render_template('errors/403.html'), 403

	item_doc = {'name': request.form['name'],'email': request.form['email']}
	db.rsvpdata.insert_one(item_doc)
	return redirect(url_for('rsvp'))


@app.route('/csv')
def csv():

	_items = db.rsvpdata.find()
	k = dumps(_items)
	j = json.dumps(k)
	
	response = make_response(j)
	response.headers["Content-Disposition"] = "attachment; filename=rsvp.json"
	return response


if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)

client.close()
	
 #read in the JSON file into Python as a string
#	rsvp_json =  open("/home/skhare/Downloads/rsvp.json").read()
#	
#	print(rsvp_json)
#	rsvp_parsed = json.loads(rsvp_json)
#        print (rsvp_parsed)
#	rsvpfile = open("/home/skhare/Downloads/rsvp.csv","r+")
#	
#	csvwriter = csv.writer(rsvpfile)
#	count = 0
#
#	for rsvp1 in rsvpfile:
#		if count == 0:
#			header = rsvp1.keys()
#			csvwriter.writerow(header)
#			count += 1 
#			csvwriter.writerow(rsvp1.values())
#
#	rsvpfile.close()
	




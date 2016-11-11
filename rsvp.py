from flask import Flask, render_template, redirect, url_for, request,make_response
from pymongo import MongoClient
import socket
import os

app = Flask(__name__)

LINK=os.environ['LINK']
TEXT1=os.environ['TEXT1']
TEXT2=os.environ['TEXT2']
LOGO=os.environ['LOGO']
COMPANY=os.environ['COMPANY']

MONGODB_HOST=os.environ['MONGODB_HOST']
client = MongoClient(MONGODB_HOST, 27017)
db = client.rsvpdata

@app.route('/')
def rsvp():
	_items = db.rsvpdata.find()
	items = [item for item in _items]
	count = len(items)
	
	hostname = socket.gethostname()

	return render_template('profile.html', counter=count, hostname=hostname, items=items, TEXT1=TEXT1, TEXT2=TEXT2, LOGO=LOGO, COMPANY=COMPANY)
	

@app.route('/new', methods=['POST'])
def new():
	item_doc = {'name': request.form['name'], 'email': request.form['email']}
	db.rsvpdata.insert_one(item_doc)
	return redirect(url_for('rsvp'))

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)

client.close()

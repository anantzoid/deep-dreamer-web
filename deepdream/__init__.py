import os
import sys
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

app.config['PENDING'] = '/var/www/deepdream/deepdream/static/pending'
app.config['ORIGINALS'] = '/var/www/deepdream/deepdream/static/originals'

@app.route('/')
def init():
     return render_template('index.html')

@app.route('/upload', methods=['POST'])
def imgupload():
	file = request.files['file']

	#cleran filename: remove . and /
	save_path = os.path.join(app.config['PENDING'], file.filename)
	print >>sys.stderr, save_path
	file.save(save_path)
	return "1" 

if __name__ == "__main__":
     app.run(debug=True)

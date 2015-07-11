import os
import sys
from flask import Flask
from flask import render_template
from flask import request
#import deepdreamnet

app = Flask(__name__)

app.config['ORIGINALS'] = '/var/www/deepdream/deepdream/static/originals'
@app.route('/')
def init():
     return render_template('index.html')

@app.route('/upload', methods=['POST'])
def imgupload():
	file = request.files['file']

	#cleran filename: remove . and /
	save_path = os.path.join(app.config['ORIGINALS'], file.filename)
	file.save(save_path)
	os.system("python /var/www/deepdream/deepdream/deepdreamnet.py "+save_path)
	return "1"
	#return deepdreamnet.init(save_path)

if __name__ == "__main__":
     app.run(debug=True)

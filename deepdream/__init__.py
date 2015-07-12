import os
import sys
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
print >>sys.stderr, os.getcwd()
app.config['PENDING'] = '/var/www/deepdream/deepdream/static/pending'
app.config['FINAL'] = '/var/www/deepdream/deepdream/static/final'

@app.route('/')
def init():
     return render_template('index.html')

@app.route('/upload', methods=['POST'])
def imgupload():
	file = request.files['file']

	#cleran filename: remove . and /
	save_path = os.path.join(app.config['PENDING'], file.filename)
	file.save(save_path)
	newfilename = file.filename.split(".")[0]+".jpeg"
	return os.path.join(app.config['FINAL'], newfilename) 

@app.route('/deepdreamed', methods=['POST'])
def converted():
	filename = request.form['file']	
	if os.path.isfile(filename):
		return filename.replace("/var/www/deepdream/deepdream","..")	
	else:
		return "pending"	

if __name__ == "__main__":
     app.run(debug=True)

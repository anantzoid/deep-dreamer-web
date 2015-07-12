#!/usr/bin/python

import sys
import os
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/deepdream/")
sys.path.append('/home/ubuntu/caffe/python')
os.environ['LD_LIBRARY_PATH'] = '/usr/local/cuda-7.0/lib64' 

'''
PROJECT_DIR = '/home/ubuntu/.virtualenvs/deepdream'
activate_this = os.path.join(PROJECT_DIR, 'bin', 'activate_this.py')
execfile(activate_this, dict(__file__=activate_this))
sys.path.append(PROJECT_DIR)
'''


from deepdream import app as application
application.secret_key = '123'

#!/usr/bin/python3
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/capstone/")

from capstone import app as application
application.secret_key = 'This is a special key'

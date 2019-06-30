#!/usr/bin/env python
from werkzeug.debug import DebuggedApplication
from flask_wtf.csrf import CSRFProtect
from flask import Flask

app = Flask(__name__)
app.secret_key = 'very secret key'
csrf = CSRFProtect(app)
app.config['TEMPLATES_AUTO_RELOAD'] = True

import app.views

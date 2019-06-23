#!/usr/bin/env python
from werkzeug.debug import DebuggedApplication
from flask_wtf.csrf import CSRFProtect
from flask import Flask
# import app.main.app
from app import app

dbg = DebuggedApplication(app, evalex=True)
app.run(debug = True)

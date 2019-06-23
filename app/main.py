#!/usr/bin/env python
from werkzeug.debug import DebuggedApplication
from flask_wtf.csrf import CSRFProtect
from flask import Flask

app = Flask(__name__)
app.secret_key = 'very secret key'
app = DebuggedApplication(app, evalex=True)
csrf = CSRFProtect(app)

import views

if __name__ == "__main__":
    app.run(debug = True, host='0.0.0.0')

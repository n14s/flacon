#!/usr/bin/env python3

from flask import Flask
from views import views

app = Flask(__name__) # initializes app
app.register_blueprint(views, url_prefix="/views")

if __name__ == '__main__':
    app.run(debug=True, port=8000) #debug=true refreshes site upon file changes

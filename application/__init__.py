from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from application import forms

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = 'fbb57fd4252ef020c0aa4ec031e1dd90'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://zyswrbyr:DmzYi5lA-BLRXGzr_wESfKpDPBKKQxXF@lucky.db.elephantsql.com/zyswrbyr'
db = SQLAlchemy(app)

from application import models


from application import routes

if __name__ == '__main__':
    app.run()
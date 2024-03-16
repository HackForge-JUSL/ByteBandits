from flask import Flask, request, session, jsonify
from flask_cors import CORS
from config import ApplicationConfig
from models import db 


app = Flask(__name__)
app.config.from_object(ApplicationConfig)
cors = CORS(app)
db.init_app(app) 




if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

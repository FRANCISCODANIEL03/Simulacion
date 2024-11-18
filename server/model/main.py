from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from train_algorith import predict

app = Flask(__name__)
CORS(app)




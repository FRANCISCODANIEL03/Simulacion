from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from train_algorith import predict

app = Flask(__name__)
CORS(app)

@app.route("/metrics", methods = ["GET"])
@cross_origin()
def metrics():
    f1score, precision, recall = predict()
    return jsonify([
        {
            "name":"F1 score",
            "porcent":f1score
        },
        {
            "name":"Precision",
            "porcent":precision
        },
        {
            "name":"Recall",
            "porcent":recall
        }
    ])

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)





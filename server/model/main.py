from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from train_algorith import predict
from metrics import predict_acc

app = Flask(__name__)
CORS(app)

@app.route("/metrics", methods = ["GET"])
@cross_origin()
def metrics():
    accuracy = predict_acc()
    f1score, precision, recall = predict()
    return jsonify([
        {
            "name":"Accuracy",
            "porcent":accuracy
        },
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
    app.run()





from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from metrics import pred_metrics
from polynomial_k import pred_reduced_f1s

app = Flask(__name__)
CORS(app)

@app.route("/metrics2", methods = ["GET"])
@cross_origin()
def metrics():
    F1_score, Pres, recall = pred_metrics()
    #F1_score2, Pres2, recall2 = pred_metrics2()
    return jsonify([
        {
            "name":"F1 score ",
            "porcent":F1_score
        },
        {
            "name":"Precision",
            "porcent":Pres
        },
        {
            "name":"Recall",
            "porcent":recall
        }
      
    ])

if __name__ == '__main__':
    app.run()

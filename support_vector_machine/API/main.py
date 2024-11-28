from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from metrics import pred_f1score_r, pred_f1score_r2, pred_f1score_c
from polynomial_k import pred_reduced_f1s

app = Flask(__name__)
CORS(app)

@app.route("/metrics2", methods = ["GET"])
@cross_origin()
def metrics():
    F1s_r = pred_f1score_r()
    F1s_r2 = pred_f1score_r2()
    F1s_c = pred_f1score_c()
    F1s_r3 = pred_reduced_f1s()
    return jsonify([
        {
            "name":"F1 score dataset reducido",
            "porcent":F1s_r
        },
        {
            "name":"F1 score dataset reducido 2",
            "porcent":F1s_r2
        },
        {
            "name":"F1 score dataset completo",
            "porcent":F1s_c
        },
        {
            "name":"F1 score dataset reducido 3",
            "porcent":F1s_r3
        }
    ])

if __name__ == '__main__':
    app.run()

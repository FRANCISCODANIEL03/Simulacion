from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from decision_tree import pred_sin_escalar, pred_escalar

app = Flask(__name__)
CORS(app)

@app.route("/tree", methods = ["GET"])
@cross_origin()
def metrics():
    resul1, resul2 = pred_escalar()
    resul3, resul4 = pred_sin_escalar()
    return jsonify([
        {
            "name":"f1_score WITHOUT preparation train:",
            "porcent":resul1
        },
        {
            "name":"f1_score WITH preparation train:",
            "porcent":resul2
        },
        {
            "name":"f1_score WITHOUT preparation val:",
            "porcent":resul3
        },
        {
            "name":"f1_score WITH preparation val:",
            "porcent":resul4
        }
    ])

if __name__ == '__main__':
    app.run()

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def fake_query(td_id):
    pass


@app.route('/votes')
def hello_world():
    td_id = request.args.get('td_id')
    fake_query(td_id)
    import time
    time.sleep(2)
    return jsonify({
        "TD_Name": "Gerry Adams",
        "Bio": "Man of the People",
        "Image":"https://www.sinnfein.ie/files/images/orig/2013/GerryAdamsWeb3001.jpg",
        "Ta": 100,
        "Nil": 50,
        "Staonaim": 20
    })


if __name__ == '__main__':
    app.run()

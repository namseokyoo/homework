from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/order', methods=['POST'])
def post_order():
    name = request.form['name']
    amount = request.form['amount']
    address = request.form['address']
    phone_number = request.form['phone_number']

    new_order = {
        "name": name,
        "amount": amount,
        "address": address,
        "phone_number": phone_number
    }
    db.order.insert_one(new_order)
    return jsonify({
        'result': 'success',
        'msg': '주문에 성공하였습니다.'
    })


@app.route('/order', methods=['GET'])
def get_order():
    orders = list(db.order.find({}, {'_id': 0}))
    return jsonify({
        'result': 'success',
        'order': orders
    })


if __name__ == "__main__":
    app.run('localhost', 5001)

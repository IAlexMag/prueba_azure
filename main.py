from flask import Flask, jsonify, redirect, render_template, request

app = Flask(__name__)


@app.route('/', methods = ['GET'])
def index():
    if request.method == ['GET']:
        data = {
            'user' : 'random',
            'created' : '2024-05-19',
            'more' : {'name' : 'Alexander', 'age' : 25, 'email' : 'unknowgmail.com'}
        }
        return jsonify(data)




if __name__ == '__main__':
    app.run(host='0.0.0.0')
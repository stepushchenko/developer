from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    numbers = {'string': 0, 'f2': 1, '15': 6, 'g3': -8, '19': 19, 'b2c5f': 11, '09': 90}
    return render_template('index.html', numbers=numbers)


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def render_send():
    return '...'


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)

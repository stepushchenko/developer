from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<number>/')
def index(number):
    text = f"Ваше число {number}, умноженное на 2:"
    number = float(number) * 2
    return render_template('index.html', number=number, text=text)


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)

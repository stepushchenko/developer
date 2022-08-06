from flask import Flask

app = Flask(__name__)


@app.route("/")
def another_page():
    return '''
    <!DOCTYPE html>
    <html>
        <head>
            <title>Home page</title>
            <meta charset="utf-8">
        </head>
        <body>
            <p>Hello, Flask!</p>
        </body>
    </html>
    '''


if __name__ == '__main__':
    app.run(host='localhost', port=5000)

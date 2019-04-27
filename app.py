from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    # Show the main page of the shader repo. It should display the most popular shaderpacks of the month in a grid view
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

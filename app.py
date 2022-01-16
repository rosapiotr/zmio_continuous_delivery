from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    response = {"Hello": "World"}
    return response


if __name__ == "__main__":
    app.run(debug=True)
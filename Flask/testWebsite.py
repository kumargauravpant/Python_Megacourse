import flask

app=flask.Flask(__name__)

@app.route('/')
def home():
    return "Homepage here!"


if __name__=="__main__":
    app.run(debug=True)
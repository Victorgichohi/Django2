from flask import Flask

app=Flask(__name__)

@app.route('/')
def index(name="james"):
    return "hello {}".format(name)

app.run(debug=True , port=8000 , host='0.0.0.0')

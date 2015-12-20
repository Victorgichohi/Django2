from flask import Flask
from flask import request
app=Flask(__name__)

@app.route('/')
def index(name="james"):
    name=request.args.get('name',name)
    return "hello {}".format(name)

app.run(debug=True , port=8000 , host='0.0.0.0')

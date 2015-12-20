from flask import Flask

app=Flask(__name__)

@app.route('/')
@app.route('/<name>')
def index(name="james"):
    # name=request.args.get('name',name)
    return "hello {}".format(name)

@app.route('/add/<int:num1>/<int:num2>')
def add(num1,num2):
    return "{}+{}={}".format(num1,num2,num1+num2)

app.run(debug=True , port=8000 , host='0.0.0.0')

from flask import Flask,url_for,redirect,request
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/save',methods=['POST'])
def save():
    import pdb; pdb.set_trace()

    return redirect (url_for('index'))
app.run(debug=True, port=8000, host='0.0.0.0')

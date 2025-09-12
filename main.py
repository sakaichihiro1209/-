from flask import Flask, render_template, make_response, request
import json
from cookie_service import cookie

app = Flask(__name__)

@app.route('/resp')
def resp():

    return render_template('regist_group.html')

@app.route('/regist-group-post', methods=['POST'])
def regist_group():
    group_name=request.form['group']
    cookie_service=cookie()
    responce = cookie_service.set_group(group_name)
    return responce

@app.route('/view')
def view():
    cookie_service=cookie()
    group_name = cookie_service.get_group()
    return render_template('view.html', group_name = group_name)
app.run(debug=True)

from flask import Flask, render_template, make_response, request
import json
from cookie_service import cookie
import sqlite3
from DBservice import DBservice
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

@app.route('/')
def view():
    link="http://www.kms.ac.jp/files/1517/3528/3269/igaku1_2025.pdf#toolbar=0&view=Fit&page="+str(9)+""
    return render_template('depertment_detail.html',link=link)
@app.route('/now_depertment')
def now_depertment():
    dbservice=DBservice()
    cookie_service=cookie()
    group_name = cookie_service.get_group()
    if group_name==0:
        return render_template('view.html', now = "",next="",day="")
    else:
        
        dbservice.get_topview(group_name)
        
    page=dbservice.get_page(dbservice.now_depertment)
    pdfpage=int(page)+5
    
    link="http://www.kms.ac.jp/files/1517/3528/3269/igaku1_2025.pdf#toolbar=0&view=Fit&page="+str(pdfpage)+""
    return render_template('depertment_detail.html', link=link)


    
    
app.run(debug=True)

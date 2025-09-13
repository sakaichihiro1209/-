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
    dbservice=DBservice()
    cookie_service=cookie()
    group_name = cookie_service.get_group()
    if group_name==0:
        
        nowlink="http://www.kms.ac.jp/files/1517/3528/3269/igaku1_2025.pdf"
        nextlink="http://www.kms.ac.jp/files/1517/3528/3269/igaku1_2025.pdf"
        return render_template('view.html', now = "班を登録してください",next="班を登録してください",day="班を登録してください",nowlink=nowlink,nextlink=nextlink)
    else:
        
        dbservice.get_topview(group_name)
        nowpage=dbservice.get_page(dbservice.now_depertment)
        nowpdfpage=int(nowpage)+7
        nextpage=dbservice.get_page(dbservice.next_depertment)
        nextpdfpage=int(nextpage)+7
        nowlink="http://www.kms.ac.jp/files/1517/3528/3269/igaku1_2025.pdf#toolbar=0&view=Fit&page="+str(nowpdfpage)+""
        nextlink="http://www.kms.ac.jp/files/1517/3528/3269/igaku1_2025.pdf#toolbar=0&view=Fit&page="+str(nextpdfpage)+""
        
        return render_template('view.html', now = dbservice.now_depertment,next=dbservice.next_depertment,day=dbservice.first_day,nowlink=nowlink,nextlink=nextlink)

    
app.run(debug=True)

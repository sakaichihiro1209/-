from flask import Flask, render_template, make_response, request
import json
from cookie_service import cookie
import sqlite3
from DBservice import DBservice
app = Flask(__name__, static_folder='./templates/static_data')

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
        return render_template('view.html', now = "班を登録してください",next="班を登録してください",day="班を登録してください")
    else:
        
        dbservice.get_topview(group_name)
        page=int(dbservice.get_page(dbservice.now_depertment))+5
        image1 = 'static_data/'+'{0:04}'.format(page) +'.jpg'
        image2 = 'static_data/'+'{0:04}'.format(page+1) +'.jpg'
        image3 = 'static_data/'+'{0:04}'.format(page+2) +'.jpg'
        next_page=int(dbservice.get_page(dbservice.next_depertment))+5
        image4 = 'static_data/'+'{0:04}'.format(next_page) +'.jpg'
        image5 = 'static_data/'+'{0:04}'.format(next_page+1) +'.jpg'
        image6 = 'static_data/'+'{0:04}'.format(next_page+2) +'.jpg'

        
        return render_template('view.html', now = dbservice.now_depertment,next=dbservice.next_depertment,day=str(dbservice.first_day).replace(" 00:00:00",""),image1=image1,image2=image2,image3=image3,image4=image4,image5=image5,image6=image6,now_drive=dbservice.now_drive,next_drive=dbservice.next_drive)




app.run(debug=True)

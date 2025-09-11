from flask import Flask, render_template, make_response, request
import datetime
import json
class cookie:
    def set_group(self,group):
        max_age = 30
        expires = int(datetime.datetime.now().timestamp()) + max_age
        response = make_response(render_template("cookie.html"))
        user_info = {'group':group} 
        response.set_cookie("group_name", value=json.dumps(user_info), expires=expires)
        return response
    def get_group(self):
        user_info = request.cookies.get('group_name')
        if user_info is not None:
            group_name = json.loads(user_info)
        return group_name['group']
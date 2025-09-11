from flask import Flask, render_template, make_response, request
import json
import datetime
 
class cookie_service:
    group=""
    def get_group(self):
        group_cookie=request.cookie.get("group")
        if group_cookie is not None:
            group_json = json.loads(group_cookie)
            self.group=group_json.group
        return self.group
    def set_group(self,group):
        expires = int(datetime.datetime.now().timestamp()) +30
        response = make_response(render_template("cookie.html"))
        user_info = {'group':group} 
        response.set_cookie("groupname", value=json.dumps(user_info), expires=expires)
        return response


import json
from cookie_service import cookie
import sqlite3
from DBservice import DBservice

dbservice=DBservice()
dbservice.get_topview("G")

print(dbservice.first_day)

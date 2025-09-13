import sqlite3

class scheduleDB:
    def __init__(self):
        dbname = 'schedule.db'
        conn = sqlite3.connect(dbname)
        self.cur = conn.cursor()
    def schedule_tabel(self,group):
        sql="SELECT * FROM schedule_table3 WHERE group_name = 'group"+group+"';"
        self.cur.execute(sql)
        return self.cur.fetchone()
    def week_table(self):
        respons=self.cur.execute("SELECT * FROM week_table2 ;")
        self.cur.arraysize = 1000
        week_list=self.cur.fetchall()
        return week_list
    def depertment_table(self,depertment):
        sql="SELECT * FROM depertment_table2 WHERE depertment='"+depertment+"';"
        respons=self.cur.execute(sql)
        return respons.fetchone()

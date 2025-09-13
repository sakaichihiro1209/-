from datetime import datetime
from scheduleDB import scheduleDB

class DBservice:
    group=""
    def __init__(self):



        # 実験用に日付指定
        # self.date=datetime.now()
        self.date=datetime.strptime("2025-09-17",'%Y-%m-%d')
        self.now_week=None
        self.next_depertment_week=None
        self.infra=scheduleDB()
    next_depertment=""
    next_startday=""
    def get_topview(self,group):
        


        # テキスト型の開始日と終了日weel_listに
        week_list=self.infra.week_table()
        # 日付型に変更して今の日付が何週にあたるのか確認
        for row in week_list:
            start_day=datetime.strptime(row[1],'%Y-%m-%d')
            finish_day=datetime.strptime(row[2],'%Y-%m-%d')
            if (start_day<=self.date)and(self.date<=finish_day):
                self.now_week=int(row[0])
            else:
                pass
                
        group_schedule=self.infra.schedule_tabel(group)

        # 行番号は週数-31なので
        self.now_depertment=group_schedule[self.now_week-31]
        # 次の週は-30だけど同じだったら-29
        if self.now_depertment==group_schedule[self.now_week-30]:
            # 二週間の診療科だったということだから
            self.next_depertment=group_schedule[self.now_week-29]
            self.next_depertment_week=self.now_week+2
        else:
            # 一週間の診療科だったということだから
            self.next_depertment=group_schedule[self.now_week-30]
            self.next_depertment_week=self.now_week+1
        for row in week_list:
            if int(row[0])==self.next_depertment_week:
                self.first_day=datetime.strptime(row[1],'%Y-%m-%d')
            else:
                print(row[1])
    def get_page(self,depertment):
        depertment_data=self.infra.depertment_table(depertment)
        return depertment_data[1]


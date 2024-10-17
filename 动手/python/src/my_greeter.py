import datetime
import time

class MyGreeter:
    
    def greeting(self):
        #获取当前日期时间
        now = datetime.datetime.now()
        #获取当前时间小时
        nowHour=datetime.datetime.now().hour
        #nowTime=time.strftime("%H:%M:%S", time.localtime()) 
        print("Now Time is "+str(now)+". hour is "+str(nowHour))

        #进行当前小时数比较，判断早中晚，并提示问候
        if 6<=nowHour<12:
            print("Good morning")
        elif 12<=nowHour<18:
            print("Good afternoon")
        elif 18<=nowHour or nowHour<6:
            print("Good afternoon")
        else:
            print("No Time, please run again")

if __name__ == '__main__':
    MyGreeter.greeting()
    

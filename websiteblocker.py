import time
from datetime import datetime as dt

hosts_temp=r"C:\Users\koduk_er34\Desktop\Python apps\app3\hosts"
hosts_path ="C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com","www.buzzfeed.com","buzzfeed.com"]


while True:
# the if statement says if the time is between 8 and 5 then print working hours.
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Working hours....")
        with open(hosts_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.seek(0,2)
                    file.write(redirect+" "+ website+"\n")
    else:
     #prevents redirect during non-working hours
        with open(hosts_path, 'r+') as file: #opening the host file in read and append method
            content=file.readlines() # store the lines in content list
            file.seek(0) # tells python to put the pointer in the first line
            for line in content:
                if not any(website in line for website in website_list):    # if any of the websites in currently in the content list then the line is written in the host file.
                    file.write(line)
                file.truncate() # cuts off anything under the content line. existing content list is deleted from the hosts file
        print("Fun hours.....")
    time.sleep(5)

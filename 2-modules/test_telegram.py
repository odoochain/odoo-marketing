import requests 
from datetime import datetime
import schedule
import time

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("current time :", current_time)
img="http://image.careers-portal.co.za/f_output.jpg " 

def job():
    text="test" 
    r = requests.get('https://api.telegram.org/bot5334866499:AAHmcLwp_Eoz-sy-NqmFFwHdSr1cbhIfurg/sendMessage?chat_id=@yvan_fw_channel&parse_mode=markdown&text='+text)

schedule.every(10).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

"""
import requests  
text="testing [](http://image.careers-portal.co.za/f_output.jpg) (test)  "
for i in range(len(text)):
    if (text[i]=="[" and text[i+1]=="]" and text[i+2]=="("):
        j=i+3
        while text[j]!=")":
            j=j+1
        img=text[i+3:j]
text=text.replace("("+img+")","") 
 
print(text)  
print(img)
r = requests.get('https://api.telegram.org/bot5334866499:AAHmcLwp_Eoz-sy-NqmFFwHdSr1cbhIfurg/sendMessage?chat_id=@yvan_fw_channel&parse_mode=markdown&text='+"[​​​​​​​​​​​]("+img+")"+text)
"""

"""
import requests  
import re
text="testing #http://image.careers-portal.co.za/f_output.jpg# (test) #https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Stack_Overflow_logo.svg/200px-Stack_Overflow_logo.svg.png#"
img=(re.search("#(.+?)#", text).group(1)) 
#text=text.replace("#"+img+"#","") 
print(text)  
print(img)
r = requests.get('https://api.telegram.org/bot5334866499:AAHmcLwp_Eoz-sy-NqmFFwHdSr1cbhIfurg/sendMessage?chat_id=@yvan_fw_channel&parse_mode=markdown&text='+"[​​​​​​​​​​​]("+img+")"+text)
"""
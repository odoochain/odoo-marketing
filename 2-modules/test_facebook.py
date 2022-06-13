import requests
#Your Access Keys

"""
page_id_1 = 111693221538816 # 109625408413423
facebook_access_token_1 = 'EAAHiliwLQMkBADSxwsnQp5hmUcWpD6qZBBnlXONgDsZAQ9rcZAVSiZC6T2AZC2HoKJNYvW6Y0OlqObSh4WssZAm6d1FFm6Nz7VxZBx5mqykEYZAxnZA0uFr6NlqomXcAhQF4uNuSC13kgy3kGV9vKTyG0tEqp7x6XnkvGDfVwRZBVWhMJjplPaY4ww'
msg = 'new TEST'
post_url = 'https://graph.facebook.com/{}/feed'.format(page_id_1)
payload = {
'message': msg,
'access_token': facebook_access_token_1
}
r = requests.post(post_url, data=payload)
print(r.text)
"""
"""
page_id_1 = 111693221538816 # 109625408413423
facebook_access_token_1 = 'EAAYTNS3KDDsBAPq6E3en9sJfwkBdUZCZBTZAFMYTnyPp80F1k5Xb0ikIpIwE1DogGZCaGtBYmdZAY5mPxi8lA1IKy2NTheXLURhwGRsESoeF7KEZCsg3O4KI44PLORSsmrAPdH9sPGp25Rw8BLHc2zI0NKjjjq5Y2uQnmqiNSN8XqB90UiGLMQmRtZBUZAimC57bkNGB5Wnsv95pgAoBVGby'
image_url = 'https://graph.facebook.com/{}/photos'.format(page_id_1)
image_location =   'http://image.careers-portal.co.za/f_output.jpg'
msg = 'new TEST'
img_payload = {
'message': msg,
'url' : image_location,
'access_token': facebook_access_token_1
}
r = requests.post(image_url, data=img_payload)
print(r.text)
"""

import schedule
import time
def sendPost1():
        page_id_1 =109625408413423  # 111693221538816
        facebook_access_token_1 = 'EAAYTNS3KDDsBAFC7NOA9b2dRDPCXpYYk2pnR3RcVVZBIqpzhZBfiIboZA2ZAYq3VuUknvDZC8hk4fBlqfDZC9KWLAI6jcuogR3Ghc5hszwDoZAmcP7G6ZAvg7ZChngIFUVa2IvToKTC3G115HtPuuKhmM8OvsCmNqUdwGzLOAgk4q6u6xsBNlr1JMDSepqDOZA2xrvTRrzQosxn76YbX81k5uz'
        msg = ' test 100001'
        post_url = 'https://graph.facebook.com/{}/feed'.format(page_id_1)
        payload = {
        'message': msg,
        'access_token': facebook_access_token_1
        }
        r = requests.post(post_url, data=payload)
        print(r.text)




date="14:28"
schedule.every().day.at(date).do(sendPost1)

while True:
    schedule.run_pending()
    #time.sleep(1)


import requests
import time
import re
import json
from random import randint
from datetime import datetime,timedelta
from dingtalkchatbot.chatbot import DingtalkChatbot

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }

#获取登录code
def get_code(location):
    code_pattern = re.compile("(?<=access=).*?(?=&)")
    code = code_pattern.findall(location)[0]
    #print(code)
    return code
 
#登录
def login(user,password):
    url1 = "https://api-user.huami.com/registrations/+86" + user + "/tokens"
    headers = {
        "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
    "User-Agent":"MiFit/4.6.0 (iPhone; iOS 14.0.1; Scale/2.00)"
        }
    data1 = {
        "client_id":"HuaMi",
        "password":f"{password}",
        "redirect_uri":"https://s3-us-west-2.amazonaws.com/hm-registration/successsignin.html",
        "token":"access"
        }
    r1 = requests.post(url1,data=data1,headers=headers,allow_redirects=False)
    print(r1.text)
    location = r1.headers["Location"]
    #print(location)
    try:
        code = get_code(location)
    except:
        return 0,0
    print("access_code获取成功！")
    print(code)
     
    url2 = "https://account.huami.com/v2/client/login"
    data2 = {
        "app_name":"com.xiaomi.hm.health",
        "app_version":"4.6.0",
        "code":f"{code}",
        "country_code":"CN",
        "device_id":"2C8B4939-0CCD-4E94-8CBA-CB8EA6E613A1",
        "device_model":"phone",
        "grant_type":"access_token",
        "third_name":"huami_phone",
        } 
    r2 = requests.post(url2,data=data2,headers=headers).json()
    login_token = r2["token_info"]["login_token"]
    print("login_token获取成功！")
    print(login_token)
    userid = r2["token_info"]["user_id"]
    print("userid获取成功！")
    print(userid)
 
    return login_token,userid

 
#主函数
def main():     
    login_token = 0
    login_token,userid = login(user,password)
    if login_token == 0:
        print("登陆失败！")
        return "login fail!"
 
    t = get_time()
     
    app_token = get_app_token(login_token)
 
    date = (datetime.now() + timedelta(hours=8)).strftime("%Y/%m/%d %H:%M:%S")
 
    with open('data_json.txt','rt') as f:
        data_json = f.read()
    step_pattern = re.compile("__ttl__")
    date_pattern = re.compile("__date__")
    data_json = step_pattern.sub(f"{step}",data_json)
    data_json = date_pattern.sub(f"{date}",data_json)
    url = f'https://api-mifit-cn.huami.com/v1/data/band_data.json?&t={t}'
    head = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.12(0x17000c2d) NetType/WIFI Language/zh_CN',
        'apptoken': f'{app_token}'
        }
     
    data = {
        'data_json': f'{data_json}',
        'userid': f'{userid}',
        'device_type': '0',
        'last_sync_data_time': '1629913654',
        'last_deviceid': 'DA932FFFFE8888E8',
        }
 
    response = requests.post(url, data=data, headers=head).json()
    print(response)
    result = "时间："+date+"\n" + f"账号：{user}\n密码：{password}\n步数：{step}\n状态："+ response['message']
    sendDingDing(result)
    print(result)
    return result
  
#获取时间戳
def get_time():
    url = 'http://api.m.taobao.com/rest/api3.do?api=mtop.common.getTimestamp'
    response = requests.get(url,headers=headers).json()
    t = response['data']['t']
    return t
  
#获取app_token
def get_app_token(login_token):
    url = f"https://account-cn.huami.com/v1/client/app_tokens?app_name=com.xiaomi.hm.health&dn=api-user.huami.com%2Capi-mifit.huami.com%2Capp-analytics.huami.com&login_token={login_token}&os_version=4.1.0"
    response = requests.get(url,headers=headers).json()
    app_token = response['token_info']['app_token']
    print("app_token获取成功！")
    print(app_token)
    return app_token

# 钉钉机器人通知
def sendDingDing(msg):
    print('正在发送钉钉机器人通知...')
    webhook = 'https://oapi.dingtalk.com/robot/send?access_token=fadb9756052d6bbafb45e72e10477f9ad94020ad55058903806b21209170cae0'
    secret = 'SEC024ea5ad293132c70a3439a9dbfefcb9ed5795e8c138d4c7e39406f296c286d9'
    xiaoding = DingtalkChatbot(webhook, secret=secret)  # 方式二：勾选“加签”选项时使用（v1.5以上新功能）
    xiaoding.send_text(str(msg), is_at_all=False)

#。。。。。。
def main_handler(event, context):
    return main()

#PJS
user = "15918716015"
password = "PJSfy757"
step = str(randint(45678,47869))
main()

#WSZ
user = "15817173886"
password = "WSZfy979"
step = str(randint(17760,19999))
main()

#ZWT
user = "15750831200"
password = "qq1314520"
step = str(randint(34567,36666))
main()

#WXF
user = "18219317399"
password = "WXFwxf666"
step = str(randint(10001,12345))
main()

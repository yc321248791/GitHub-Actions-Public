import requests
import random

mi_user = "手**机**号"
mi_pwd = "密*******码"
mi_step = str(random.randint(75792,78520))


url = "https://bu.txmmp.cn/api/bf.php?mobile=" + mi_user + "&password=" + mi_pwd + "&step=" + mi_step


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67'
}

res = requests.get(url,headers=headers)
data = res.text

try:
    print(data) 
except ConnectionError:
    print('拒绝连接')


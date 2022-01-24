# GitHub-Actions-Public

## **关于 [小米运动](https://app.mi.com/details?id=com.xiaomi.hm.health) 自动提交步数**

* 将文件 [`huami-step.yml`](https://github.com/s757129/GitHub-Actions-Public/blob/main/huami-step/huami-step.yml) 放在 [.github/workflows](https://github.com/s757129/GitHub-Actions-Public/tree/main/.github/workflows) 目录下，文件会 [`index.py`](https://github.com/s757129/GitHub-Actions-Public/blob/main/huami-step/index.py) 自动执行

* **钉钉自定义机器人** [`chatbot.py`](https://github.com/zhuifengshen/DingtalkChatbot/blob/master/dingtalkchatbot/chatbot.py) 配置

* **部署账号密码步数** [`index.py`](https://github.com/s757129/GitHub-Actions-Public/blob/main/huami-step/index.py) 如下：
```python
# 【华米科技】小米运动APP
user = "1*********6" # 手机号
password = "1******8" # 密码
step = str(randint(17760,19999)) # 随机步数
```



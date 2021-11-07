# 华米科技&小米运动 · 刷步数

* **钉钉自定义机器人** [`chatbot.py`](https://github.com/zhuifengshen/DingtalkChatbot/blob/master/dingtalkchatbot/chatbot.py)

项目源码地址：[DingtalkChatbot](https://github.com/zhuifengshen/DingtalkChatbot)

* **主配置文件** `workflows.py`

```bash
#【华米科技】小米运动APP
user = "1*********6" #手机号
password = "1******8" #密码
step = str(randint(17760,19999)) #随机步数
```

* **GitHub Actions** `workflows.yml`
放在 `.github/workflows` 文件夹下 `workflows.yml` 会自动执行

* **关于时间的问题**

注：GitHub的时间格式是UTC
1、`date` 时间格式是本地时间
2、`date_time` 时间格式是本地时间+8h
配置腾讯云函数时请自行修改
位置在主配置 `workflows.py` 的第105行

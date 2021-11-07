# **华米科技&小米运动 · 刷步数**

* **钉钉自定义机器人** [`chatbot.py`](https://github.com/zhuifengshen/DingtalkChatbot/blob/master/dingtalkchatbot/chatbot.py)

项目源码地址：[DingtalkChatbot](https://github.com/zhuifengshen/DingtalkChatbot)

# 一、关于配置文件

* 主配置文件 `workflows.py`

```bash
#【华米科技】小米运动APP
user = "1*********6" #手机号
password = "1******8" #密码
step = str(randint(17760,19999)) #随机步数
```

* API配置文件 `data_json.txt`
&ensp;修复 by.Quiet
&ensp;QQ群：60067386

* GitHub Actions `workflows.yml`
&ensp;将文件放在 `.github/workflows` 文件夹下
&ensp;`workflows.yml` 会自动执行主配置文件

# 二、关于时间问题
&ensp;注：GitHub的时间格式是UTC
* `date` 时间格式是本地时间
* `date_time` 时间格式是本地时间+8h
&ensp;如配置腾讯云函数等可自行修改
&ensp;位置在主配置 `workflows.py` 的第105行

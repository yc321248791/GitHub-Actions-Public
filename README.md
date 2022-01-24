# GitHub-Actions-Public

* **钉钉自定义机器人** [`chatbot.py`](https://github.com/zhuifengshen/DingtalkChatbot/blob/master/dingtalkchatbot/chatbot.py)

项目源码地址：[DingtalkChatbot](https://github.com/zhuifengshen/DingtalkChatbot)

# 关于配置文件

* 主配置文件 `workflows.py`

```bash
#【华米科技】小米运动APP
user = "1*********6" #手机号
password = "1******8" #密码
step = str(randint(17760,19999)) #随机步数
```

* API配置文件 `data_json.txt`

修复 by . Quiet  
QQ群：60067386

* GitHub Actions `workflows.yml`

将文件放在 `.github/workflows` 文件夹下  
`workflows.yml` 会自动执行主配置文件

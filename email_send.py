import smtplib
import json
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

configure = json.load(open("configure.json", "r"))
receivers = ["1240682960@qq.com"]
def send_mail(target):
    message = MIMEText("{},{},{}".format(target.get("title"),target.get("link"),target.get("time")), "plain", "utf-8")
    message['From'] = formataddr(('我的爬虫',configure.get("MAIL_USER")))
    message['To'] = formataddr(('用户',receivers[0]))

    subject = "教务新消息"
    message["Subject"] = Header(subject, 'utf-8')



    smtpObj = smtplib.SMTP(configure.get("MAIL_SERVER"),25)
    # smtpObj.connect(configure.get("MAIL_SERVER"), 25)
    smtpObj.login(configure.get("MAIL_USER"), configure.get("MAIL_PASSWORD"))
    smtpObj.sendmail(configure.get("MAIL_USER"), receivers, message.as_string())

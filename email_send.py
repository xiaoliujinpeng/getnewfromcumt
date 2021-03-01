import smtplib
import json
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
import os.path


def send_email(target):
    filedir = os.path.dirname(os.path.abspath(__file__))
    conf_file=os.path.join(filedir,"configure.json")
    configure = json.load(open(conf_file, "r"))
    receivers = ["1240682960@qq.com"]

    message = MIMEText("{},{},{}".format(target.get('time'),target.get("title"),target.get("link")), "plain", "utf-8")
    message['From'] = formataddr(('我的爬虫',configure.get("MAIL_USER")))
    message['To'] = formataddr(('用户',receivers[0]))

    subject = "教务新消息"
    message["Subject"] = Header(subject, 'utf-8')



    smtpObj = smtplib.SMTP(configure.get("MAIL_SERVER"),25)
    # smtpObj.connect(configure.get("MAIL_SERVER"), 25)
    smtpObj.login(configure.get("MAIL_USER"), configure.get("MAIL_PASSWORD"))
    smtpObj.sendmail(configure.get("MAIL_USER"), receivers, message.as_string())

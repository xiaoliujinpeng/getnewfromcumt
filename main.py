from getHtml import get_focus_news_list
import os.path
import os
import csv
from email_send import send_email
from logs import logger

def write_file(f):
    csvf = csv.writer(f)
    data = get_focus_news_list()
    result=map(lambda x:list((x.get("title"),x.get("link"),x.get("time"))),data)
    csvf.writerows(result)
def check_file(filename):
    if not os.path.exists(filename):
        with open(filename, "a",encoding="utf-8",newline='') as f:
            write_file(f)
        return False
    return True
    


def main():
    if not check_file("data.csv"):
        logger.info("未检测到data.csv文件,创建了data.csv文件")
        return
    
    f=open("data.csv","r+",encoding="utf-8",newline='')
    if f.read() == '':
        logger.info("检测到data.csv文件为空,初始化内容")
        write_file(f)
        f.flush()
        f.close()
        return
    f.seek(0)
    read = csv.reader(f)
    titles=[each[0] for each in read]
    
    new = get_focus_news_list()
    logger.info("获取到教务网内容,{}".format(new))
    new_titles = map(lambda x: x.get("title"), new)
    target_title = filter(lambda x: not (x in titles), new_titles)
    target=filter(lambda x:x.get("title") in target_title,new)
    for each in target:
        send_email(each)
        logger.info("发送邮件到用户")

    with open("data.csv", "w", encoding="utf-8", newline='') as f:
        write_file(f)
        logger.info("重新写入data.csv，覆盖原有的内容")


if __name__ == "__main__":
    main()
from getHtml import get_focus_news_list
import os.path
import os
import csv
from email_send import send_email

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
        return
    
    f=open("data.csv","r+",encoding="utf-8",newline='')
    if f.read() == '':
        write_file(f)
        f.flush()
        f.close()
        return
    f.seek(0)
    read = csv.reader(f)
    titles=[each[0] for each in read]
    
    new=get_focus_news_list()
    new_titles = map(lambda x: x.get("title"), new)
    target_title = filter(lambda x: not (x in titles), new_titles)
    target=filter(lambda x:x.get("title") in target_title,new)
    for each in target:
        send_email(each)

    with open("data.csv", "w", encoding="utf-8", newline='') as f:
        write_file(f)


if __name__ == "__main__":
    main()
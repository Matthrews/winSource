# @author: sareeliu
# @date: 2022/5/2 14:46
import platform
import sys
import time

import pymysql
from getData import getData

if platform.system() in ["Windows", "Darwin"]:
    dbinfo = {
        "host": "django.chuanyun101.com",
        "user": "root",
        "password": "qq1788lover",
        "port": 3306,
        "db": "winsourcedb",
    }
else:
    dbinfo = {
        "host": "django.chuanyun101.com",
        "user": "root",
        "password": "qq1788lover",
        "port": 3306,
        "db": "winsourcedb",
    }


def save_data(data):
    conn = pymysql.connect(**dbinfo)
    c = conn.cursor()
    # item_detail_title, item_detail_href, item_detail_manufacturer_title,item_detail_addinfo
    # item_availablity_text, item_availablity_low_price, item_availablity_env, item_availablity_pdf, item_picture

    sql = "insert into myapp_product " \
          "(item_detail_title, item_detail_href,item_detail_manufacturer_title,item_detail_addinfo," \
          "item_availablity_text, item_availablity_low_price,item_availablity_env, " \
          "item_availablity_pdf,item_picture) values (%s,%s,%s,%s,%s,%s,%s,%s,%s) on duplicate key update " \
          "item_detail_href = values (item_detail_href)," \
          "item_detail_manufacturer_title = values (item_detail_manufacturer_title), " \
          "item_detail_addinfo = values (item_detail_addinfo), " \
          "item_availablity_text = values (item_availablity_text), " \
          "item_availablity_low_price = values (item_availablity_low_price), " \
          "item_availablity_env = values (item_availablity_env), " \
          "item_availablity_pdf = values (item_availablity_pdf), " \
          "item_picture = values (item_picture)"
    # print(sql)
    c.executemany(sql, data)
    conn.commit()
    c.close()
    conn.close()


try:
    searchParam = sys.argv[1]  # 'a' 第一个参数
    pagenumber = sys.argv[2]  # 1   第二个参数
    duration = int(sys.argv[3])
except:
    searchParam = input("输入搜索参数：")  # 第一个参数
    pagenumber = input("输入从第几页开始：")  # 第二个参数
    duration = int(input("输入间隔时间："))

while True:
    try:
        tip = f"当前爬取的链接搜索参数是{searchParam}，页码是第{pagenumber}页"
        print(tip)
        with open('./file.txt', mode='a+', encoding='utf-8') as f:
            f.writelines(time.strftime('%Y-%m-%d %H:%I:%S', time.localtime()) + " " + tip +"\n")
        data = getData(searchParam=searchParam, pagenumber=pagenumber)
        if not data['next_page']:
            save_data(data['data_list'])
            break
        # 存储爬取的当前页数据
        save_data(data['data_list'])
        # 把页码设置为下一页
        pagenumber = data['next_page']
        time.sleep(10)
    except (IndexError, pymysql.err.OperationalError) as e:
        print("报错信息为：" + str(e))
        duration += 60
        print("报错后进行下一轮，尝试等待时间：" + str(duration) + " 秒")
        time.sleep(duration)

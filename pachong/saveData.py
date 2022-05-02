# @author: sareeliu
# @date: 2022/5/2 14:46
import pymysql
import time
from getData import getData

dbinfo = {
    "host": "django.chuanyun101.com",
    "user": "root",
    "password": "qq1788lover",
    "port": 3306,
    "db": "winsource",
}


def save_data(data):
    conn = pymysql.connect(**dbinfo)
    c = conn.cursor()
    sql = "insert into data " \
          "(item_detail_title, item_detail_href,item_detail_manufacturer_title," \
          "item_detail_manufacturer_href,item_availablity_text, item_availablity_price, " \
          "item_availablity_pdf,item_picture) values (%s,%s,%s,%s,%s,%s,%s,%s) on duplicate key update " \
          "item_detail_href = values (item_detail_href)," \
          "item_detail_manufacturer_title = values (item_detail_manufacturer_title), " \
          "item_detail_manufacturer_href = values (item_detail_manufacturer_href), " \
          "item_availablity_text = values (item_availablity_text), " \
          "item_availablity_price = values (item_availablity_price), " \
          "item_availablity_pdf = values (item_availablity_pdf), " \
          "item_picture = values (item_picture)"

    c.executemany(sql, data)
    conn.commit()
    conn.close()


# 初始化
pagenumber = 80
searchParam = 'a'
ip = '101.35.141.230'
# ip = '198.55.106.119'
port = '8888'

ip_port = "{}:{}".format(ip, port)

# proxies = {
#     "http": "http://{}".format(ip_port),
#     "https": "https://{}".format(ip_port),
# }

proxies = {}

while True:
    print(f"当前爬取的链接搜索参数是{searchParam}，页码是第{pagenumber}页，请求IP是{ip_port}")
    # try:
    data = getData(searchParam=searchParam, pagenumber=pagenumber, proxies=proxies)
    # except:
    #     data = getData(searchParam=searchParam, pagenumber=pagenumber,proxy_ip=)
    #     pass

    if not data['next_page']:
        save_data(data['data_list'])
        break
    # 存储爬取的当前页数据
    save_data(data['data_list'])
    # 进行下一页的数据爬取
    getData(searchParam=searchParam, pagenumber=data['next_page'], proxies=proxies)
    # 把页面设置为下一页
    pagenumber = data['next_page']
    time.sleep(245)

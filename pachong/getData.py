import cfscrape
from lxml import etree


def getData(searchParam,proxies,pagenumber=19):
    # print(proxies)
    scraper = cfscrape.create_scraper(delay=10)
    # 获取网页源代码
    web_data = scraper.get(f"https://www.win-source.net/search?q={searchParam}&pagenumber={pagenumber}",proxies=proxies).text
    # print(web_data)

    tree = etree.HTML(web_data)
    current_page = tree.xpath('//div[@class="pager"]/ul/li[@class="current-page"]/span/text()')[0]
    try:
        next_page = str(tree.xpath('//div[@class="pager"]/ul/li[@class="next-page"]/a/@href')[0]).split('=')[-1]
    except:
        next_page = None
    product_item = tree.xpath('//div[@class="item-grid"]/div[@class="item-box"]/div[@class="product-item"]')
    # print(product_item)

    data_list = []
    for item in product_item:
        item_picture = item.xpath('./div[@class="picture"]/a/img/@src')[0]
        item_detail = item.xpath('./div[@class="details"]')
        for item_d in item_detail:
            item_detail_title = item_d.xpath('./h2/a/@title')[0]  # 产品型号
            item_detail_href = 'https://www.win-source.net' + item_d.xpath('./h2/a/@href')[0]
            item_detail_manufacturer_title = item_d.xpath('./div[@class="manufacturer"]/a/@title')[0]
            item_detail_manufacturer_href = item_d.xpath('./div[@class="manufacturer"]/a/@href')[0]
            item_detail_addinfo = item_d.xpath('./div[@class="add-info"]/a/div/text()')

        item_availablity = item.xpath('./div[@class="availablity"]')
        for item_a in item_availablity:
            item_availablity_text = str(item_a.xpath('./div[@class="product-title"]/text()')[0]).lstrip('\n')
            item_availablity_price = item_a.xpath('./span/text()')[0]
            # item_availablity_env = item_a.xpath('./span[2]/span/img/@src')[0]
            try:
                item_availablity_pdf = item_a.xpath('./span[2]/a/@href')[0]
            except:
                item_availablity_pdf = '无'
        tmp_tuple = (item_detail_title, item_detail_href, item_detail_manufacturer_title, item_detail_manufacturer_href,
                     item_availablity_text, item_availablity_price, item_availablity_pdf, item_picture)
        # print(item_detail_title, item_detail_href,item_detail_manufacturer_title, item_detail_manufacturer_href,item_availablity_text, item_availablity_price, item_picture)
        data_list.append(tmp_tuple)
        print(tmp_tuple)
    # print(next_page)
    return {'data_list': data_list, 'next_page': next_page}

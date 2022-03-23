import cfscrape
from lxml import etree

    # 实例化一个create_scraper对象
    scraper = cfscrape.create_scraper()
    # 请求报错，可以加上时延
    # scraper = cfscrape.create_scraper(delay = 10)
    # 获取网页源代码
    web_data = scraper.get("https://www.win-source.net/search?q=LM358&pagesize=150").text
    # print(web_data)
    tree = etree.HTML(web_data)
    product_item = tree.xpath('//div[@class="item-grid"]/div[@class="item-box"]/div[@class="product-item"]')
    # print(product_item)

    for item in product_item:
        picture = item.xpath('./div[@class="picture"]/a/img/@src')[0]
        item_detail = item.xpath('./div[@class="details"]')
        for item_d in item_detail:
            item_detail_title = item_d.xpath('./h2/a/@title')[0]
            item_detail_href = item_d.xpath('./h2/a/@href')[0]
            item_detail_manufacturer_title = item_d.xpath('./div[@class="manufacturer"]/a/@title')[0]
            item_detail_manufacturer_href = item_d.xpath('./div[@class="manufacturer"]/a/@href')[0]
        item_availablity = item.xpath('./div[@class="availablity"]')
        for item_a in item_availablity:
            item_availablity_text = str(item_a.xpath('./div/text()')[0]).split("\n")[0]
            item_availablity_price = str(item_a.xpath('./span/text()')[0]).split("\n")[0]

    # print(item_detail_title, item_detail_href, item_detail_manufacturer_title, item_detail_manufacturer_href,
    #       item_availablity_text, item_availablity_price, picture)

        return {
                'item_detail_title': item_detail_title,
                'item_detail_href': item_detail_href,
                'item_detail_manufacturer_title': item_detail_manufacturer_title,
                'item_detail_manufacturer_href':item_detail_manufacturer_href,
                'item_availablity_text':item_availablity_text,
                'item_availablity_price':item_availablity_price,
                'picture': picture
        }

# print(sensitive_sync_function())
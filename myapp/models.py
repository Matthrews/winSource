from django.db import models


# Create your models here.
class Product(models.Model):
    # item_detail_title, item_detail_href, item_detail_manufacturer_title,item_detail_addinfo
    # item_availablity_text, item_availablity_low_price, item_availablity_env, item_availablity_pdf, item_picture

    PartNo = models.CharField(verbose_name="产品名称", max_length=255, db_column='item_detail_title',
                              unique=True)  # item_detail_title
    Manufacture = models.CharField(verbose_name="制造商", max_length=256,
                                   db_column='item_detail_manufacturer_title')  # item_detail_manufacturer_title
    Catalog = models.CharField(verbose_name="目录", max_length=128, default=None, blank=True, null=True)
    Description = models.CharField(verbose_name="详情", max_length=512,
                                   db_column='item_detail_addinfo')  # item_detail_addinfo
    RohsLink = models.URLField(verbose_name="环保无铅链接", db_column='item_availablity_env')  # item_availablity_env
    ProductionPDFLink = models.URLField(verbose_name="产品详情PDF链接", default=None, blank=True,
                                        db_column='item_availablity_pdf')  # item_availablity_pdf
    Availability = models.CharField(verbose_name="产品总数量", default=None, blank=True,
                                    db_column='item_availablity_text', max_length=256)  # item_availablity_text
    LowestPrice = models.CharField(verbose_name="最低价格", max_length=128, default=None, blank=True,
                                   db_column='item_availablity_low_price')  # item_availablity_low_price
    MOQ = models.IntegerField(verbose_name="最小订购数量", default=None, blank=True, null=True)
    DetailLink = models.URLField(verbose_name="商品详情链接", db_column='item_detail_href')  # item_detail_href
    Picture = models.URLField(verbose_name="图片链接", db_column='item_picture')  # item_picture

    class Meta:
        verbose_name = "产品表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.PartNo

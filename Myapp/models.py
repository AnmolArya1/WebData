from django.db import models

class ProductData(models.Model):
    PRODUCT_NAME = models.CharField(max_length=40)
    DESCRIPTION = models.TextField(max_length=100)
    PRICE = models.BigIntegerField()
    IMAGE = models.ImageField(upload_to ="img/",null=True, blank=True)


class OrderData(models.Model):
    ORDER_ID = models.BigIntegerField()
    PRODUCT_ID = models.BigIntegerField()
    DATE = models.DateField()
    PRICE = models.BigIntegerField()
    QTY = models.CharField(max_length=100)
    IMAGE = models.ImageField(upload_to ="img/",null=True, blank=True)


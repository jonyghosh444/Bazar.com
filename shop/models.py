from django.db import models


# Create your models here.


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=54)
    category = models.CharField(max_length=50, default="")
    sub_category = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="shop/image", default="")
    desc = models.CharField(max_length=3000)
    pub_date = models.DateField()

    def __str__(self):
        return self.product_name

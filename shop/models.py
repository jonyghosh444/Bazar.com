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
        details = f"{self.product_name}___{self.category}__{self.price} Tk."
        return details


class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=54)
    email = models.CharField(max_length=100, default="")
    phone = models.IntegerField(default=0)
    message = models.CharField(max_length=2000, default="")

    def __str__(self):
        txt = f"{self.name}:- {self.message}"
        return txt


class Order(models.Model):
    item_json = models.CharField(max_length=5000)
    order_id = models.AutoField(primary_key=True)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=54)
    email = models.CharField(max_length=100, default="")
    phone = models.CharField(max_length=100, default="")
    adress = models.CharField(max_length=2000)
    city = models.CharField(max_length=2000)
    division = models.CharField(max_length=2000)
    zip_code = models.CharField(max_length=100)

    def __str__(self):
        txt = f"Orederid:##00{self.order_id} {self.name} {self.phone}"
        return txt


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        text = self.update_desc
        return text
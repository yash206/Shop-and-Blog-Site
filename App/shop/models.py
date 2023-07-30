from django.db import models


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=1000)
    category = models.CharField(max_length=100, default="")
    sub_category = models.CharField(max_length=100, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=10000)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name[:20]


class Contact(models.Model):
    query_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=50, default="")
    subject = models.CharField(max_length=50, default=0)
    message = models.CharField(max_length=3000)

    def __str__(self):
        return self.name


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add= True)

    def __str__(self):
        return 'Order' + ' ' + str(self.order_id)


def __str__(self):
    return self.update_desc[0:7] + "..."
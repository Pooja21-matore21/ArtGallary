from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=20)

    def __str__(self):
        return self.category_name

    class Meta:
        db_table = "Category"


class Mehandi(models.Model):
    mehandi_name = models.CharField(max_length=20)
    price = models.FloatField(default=200)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='Images', default='pic')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = "Mehandi"


class Payment(models.Model):
    card_no = models.CharField(max_length=16)
    cvv = models.CharField(max_length=4)
    expiry_date = models.CharField(max_length=10)
    balance = models.FloatField(default=10000)

    class Meta:
        db_table = "Payment"



class Reviews(models.Model):
    namee = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    message = models.CharField(max_length=200)

    class Meta:
        db_table = "Reviews"

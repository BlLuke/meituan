
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remov` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

import time
from django.db import models


class Purse(models.Model):
    perseid = models.AutoField(db_column='perseID', primary_key=True)  # Field name made lowercase.
    balance = models.DecimalField(blank=True, null=True,max_digits=5,decimal_places=2)
    alipayaccount = models.CharField(max_length=20, blank=True, null=True)
    wechataccount = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'Purse'


class Shipper(models.Model):
    shipperid = models.AutoField(db_column='ShipperID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=15, blank=True, null=True)  # Field name made lowercase.
    personid = models.IntegerField(db_column='PersonID', blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=15, blank=True, null=True)  # Field name made lowercase.
    positionmap = models.CharField(db_column='Positionmap', max_length=20, blank=True, null=True)  # Field name made lowercase.
    gender = models.IntegerField(db_column='Gender', blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    rankedstar = models.IntegerField(db_column='Rankedstar', blank=True, null=True)  # Field name made lowercase.
    workingstatus = models.IntegerField(db_column='WorkingStatus', blank=True, null=True)  # Field name made lowercase.
    healthproof = models.CharField(db_column='Healthproof', max_length=50, blank=True, null=True)  # Field name made lowercase.
    accountid = models.OneToOneField('Account', on_delete=models.CASCADE)
    class Meta:
        db_table = 'Shipper'


class Customer(models.Model):
    userid = models.AutoField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    gender = models.IntegerField(db_column='GENDER', blank=True, null=True)  # Field name made lowercase.
    addressid = models.OneToOneField('Address',on_delete=models.CASCADE)  # Field name made lowercase.
    purseid = models.OneToOneField('Purse',on_delete=models.CASCADE)  # Field name made lowercase.
    memership = models.IntegerField(blank=True, null=True)
    accountid = models.OneToOneField("Account",on_delete=models.CASCADE)
    class Meta:
        db_table = 'User'


class Address(models.Model):
    addressid = models.AutoField(db_column='addressID', primary_key=True)  # Field name made lowercase.
    address1 = models.CharField(max_length=30, blank=True, null=True)
    address2 = models.CharField(max_length=30, blank=True, null=False, default="")
    address3 = models.CharField(max_length=30, blank=True, null=False, default="")
    address4 = models.CharField(max_length=30, blank=True, null=False, default="")
    defaultaddr = models.IntegerField(blank=True, null=False,default=1)

    class Meta:
        db_table = 'address'


class Account(models.Model):
    accountid = models.AutoField(primary_key=True)
    password = models.CharField(max_length=128)
    is_superuser = models.IntegerField(default=0)
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    is_staff = models.IntegerField(default=0)
    is_active = models.IntegerField(default=1)
    date_joined = models.DateTimeField()


class Discount(models.Model):
    discountid = models.AutoField(primary_key=True)
    restaurantid = models.ForeignKey("Restaurant",on_delete=models.CASCADE,unique=True)
    discount1 = models.CharField(max_length=10, blank=True, null=True)
    discount2 = models.CharField(max_length=10, blank=True, null=True)
    discount3 = models.CharField(max_length=10, blank=True, null=True)
    discount4 = models.CharField(max_length=10, blank=True, null=True)
    discount5 = models.CharField(max_length=10, blank=True, null=True)
    class Meta:
        db_table = 'discount'

class Ingredient(models.Model):
    ingredientid = models.AutoField(primary_key=True)
    ingredientname = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'ingredient'


class Keywords(models.Model):
    keywordsid = models.AutoField(primary_key=True)
    keyword = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'keywords'

class Order(models.Model):
    orderid = models.AutoField(primary_key=True)
    userid = models.ForeignKey('Customer',on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=5,decimal_places=2,blank=True, null=True)
    orderstatus = models.IntegerField(blank=True, null=True)
    ordertime = models.DateTimeField(auto_now=True)
    finishtime = models.DateTimeField(auto_now=True)
    paymethod = models.IntegerField(blank=True, null=True)

class Orderhistory(models.Model):
    historyid = models.AutoField(primary_key=True)
    productid = models.ForeignKey('Products',on_delete=models.CASCADE)
    orderid = models.ForeignKey('Order',on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5,decimal_places=2,blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    shipperid = models.ForeignKey('Shipper',on_delete=models.CASCADE)
    customercomment = models.TextField(blank=True, null=True)
    rank = models.CharField(max_length=1, blank=True, null=True)
    shipaddress = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'orderhistory'


class Orderlist(models.Model):
    orderid = models.AutoField(primary_key=True)
    userid = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=5,decimal_places=2,blank=True, null=True)
    orderstatus = models.CharField(max_length=1, blank=True, null=True)
    ordertime = models.DateTimeField(blank=True, null=True)
    finishtime = models.DateTimeField(blank=True, null=True)
    paymentmethod = models.CharField(max_length=9, blank=True, null=True)

    class Meta:
        db_table = 'orderlist'


class Picture(models.Model):
    pictureid = models.AutoField(primary_key=True)
    productid = models.ForeignKey('Products',on_delete=models.CASCADE, blank=True, null=True)
    restaurantid = models.ForeignKey('Restaurant',on_delete=models.CASCADE, blank=True, null=True)
    image1 = models.CharField(max_length=60, blank=True, null=True)
    image2 = models.CharField(max_length=60, blank=True, null=True)
    image3 = models.CharField(max_length=60, blank=True, null=True)
    image4 = models.CharField(max_length=60, blank=True, null=True)
    image5 = models.CharField(max_length=60, blank=True, null=True)
    image6 = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        db_table = 'picture'


class Priority(models.Model):
    priorityid = models.AutoField(primary_key=True)
    ingredientid = models.ForeignKey('Ingredient',on_delete=models.CASCADE)
    userid = models.ForeignKey('Customer',on_delete=models.CASCADE)
    prioritytype = models.IntegerField() #1:LIKE 2:DISLIKE

    class Meta:
        db_table = 'priority'


class ProductTastetype(models.Model):
    id = models.AutoField(primary_key=True)
    tasteid = models.ForeignKey('Taste',blank=True, null=True,on_delete=models.CASCADE)
    productsid = models.ForeignKey('Products',blank=True, null=True,on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_tastetype'


class Products(models.Model):
    productid = models.AutoField(primary_key=True)
    productname = models.CharField(max_length=10, blank=True, null=True)
    restaurantid = models.ForeignKey('Restaurant',on_delete=models.CASCADE)
    producttypeid = models.ForeignKey('Producttype',on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5,decimal_places=2,blank=True, null=True)
    descrition = models.TextField(blank=True, null=True)
    monthflow = models.IntegerField(blank=True, null=True)
    weekflow = models.IntegerField(blank=True, null=True)
    ranks = models.DecimalField(max_digits=5,decimal_places=2,blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        db_table = 'products'


class Producttype(models.Model):
    producttypeid = models.AutoField(primary_key=True)
    typename = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'producttype'


class Recipe(models.Model):
    recipeid = models.AutoField(primary_key=True)
    productid = models.ForeignKey('Products',blank=False,on_delete=models.CASCADE)
    ingredientid = models.ForeignKey('Ingredient',blank=False,on_delete=models.CASCADE)

    class Meta:
        db_table = 'recipe'


class Restaurant(models.Model):
    restaurantid = models.AutoField(primary_key=True)
    smallprofile = models.CharField(max_length=60, blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    publicregisterid = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=30, blank=True, null=True)
    province = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=45, blank=True, null=True)
    county_district = models.CharField(max_length=45, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    workingtime = models.CharField(max_length=10, blank=True, null=True)
    workingstatus = models.IntegerField()
    rankedstar = models.FloatField(blank=True, null=True)
    weekflow = models.IntegerField(blank=True, null=True)
    monthflow = models.IntegerField(blank=True, null=True)
    deliverytype = models.CharField(max_length=1, blank=True, null=True)
    likessum = models.IntegerField(blank=True, null=True)
    deliveryfromprice = models.IntegerField(blank=True, null=True)
    accountid = models.OneToOneField('Account', on_delete=models.CASCADE,default=0)
    class Meta:
        db_table = 'restaurant'


class SearchRecords(models.Model):
    recordid = models.AutoField(primary_key=True)
    userid = models.ForeignKey("Customer",on_delete=models.CASCADE)
    keywordsid = models.ForeignKey("Keywords",on_delete=models.CASCADE)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'search_records'


class Taste(models.Model):
    tasteid = models.AutoField(primary_key=True)
    tastetype = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        db_table = 'taste'



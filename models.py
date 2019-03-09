# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Purse(models.Model):
    perseid = models.AutoField(db_column='perseID', primary_key=True)  # Field name made lowercase.
    balance = models.FloatField(blank=True, null=True)
    alipayaccount = models.CharField(max_length=20, blank=True, null=True)
    wechataccount = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
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

    class Meta:
        managed = False
        db_table = 'Shipper'


class User(models.Model):
    userid = models.AutoField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='USERNAME', max_length=15, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    gender = models.IntegerField(db_column='GENDER', blank=True, null=True)  # Field name made lowercase.
    addressid = models.IntegerField(db_column='ADDRESSID', blank=True, null=True)  # Field name made lowercase.
    purseid = models.IntegerField(db_column='purseID', blank=True, null=True)  # Field name made lowercase.
    memership = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'User'


class Address(models.Model):
    addressid = models.AutoField(db_column='addressID', primary_key=True)  # Field name made lowercase.
    address1 = models.CharField(max_length=30, blank=True, null=True)
    address2 = models.CharField(max_length=30, blank=True, null=True)
    address3 = models.CharField(max_length=30, blank=True, null=True)
    address4 = models.CharField(max_length=30, blank=True, null=True)
    defaultaddr = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'address'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Customer(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, blank=True, null=True)
    realname = models.CharField(max_length=30, blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    addressid = models.IntegerField(blank=True, null=True)
    purseid = models.IntegerField(blank=True, null=True)
    membership = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'


class Discount(models.Model):
    discountid = models.AutoField(primary_key=True)
    restaurantid = models.IntegerField(blank=True, null=True)
    discount1 = models.CharField(max_length=10, blank=True, null=True)
    discount2 = models.CharField(max_length=10, blank=True, null=True)
    discount3 = models.CharField(max_length=10, blank=True, null=True)
    discount4 = models.CharField(max_length=10, blank=True, null=True)
    discount5 = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discount'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Ingredient(models.Model):
    ingredientid = models.AutoField(primary_key=True)
    ingredientname = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ingredient'


class Keywords(models.Model):
    keywordsid = models.AutoField(primary_key=True)
    keyword = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'keywords'


class Orderhistory(models.Model):
    historyid = models.AutoField(primary_key=True)
    productid = models.IntegerField(blank=True, null=True)
    orderid = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    shipperid = models.IntegerField(blank=True, null=True)
    customercomment = models.TextField(blank=True, null=True)
    rank = models.CharField(max_length=1, blank=True, null=True)
    shipaddress = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orderhistory'


class Orderlist(models.Model):
    orderid = models.AutoField(primary_key=True)
    userid = models.IntegerField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    orderstatus = models.CharField(max_length=1, blank=True, null=True)
    ordertime = models.DateTimeField(blank=True, null=True)
    finishtime = models.DateTimeField(blank=True, null=True)
    paymentmethod = models.CharField(max_length=9, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orderlist'


class Picture(models.Model):
    pictureid = models.AutoField(primary_key=True)
    productid = models.IntegerField(blank=True, null=True)
    restaurantid = models.IntegerField(blank=True, null=True)
    image1 = models.CharField(max_length=60, blank=True, null=True)
    image2 = models.CharField(max_length=60, blank=True, null=True)
    image3 = models.CharField(max_length=60, blank=True, null=True)
    image4 = models.CharField(max_length=60, blank=True, null=True)
    image5 = models.CharField(max_length=60, blank=True, null=True)
    image6 = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'picture'


class Priority(models.Model):
    ingredientid = models.IntegerField(blank=True, null=True)
    userid = models.IntegerField(blank=True, null=True)
    prioritytype = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'priority'


class ProductTastetype(models.Model):
    tasteid = models.IntegerField(blank=True, null=True)
    tastetype = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_tastetype'


class Products(models.Model):
    productid = models.AutoField(primary_key=True)
    productname = models.CharField(max_length=10, blank=True, null=True)
    restaurantid = models.IntegerField(blank=True, null=True)
    producttypeid = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    descrition = models.TextField(blank=True, null=True)
    monthflow = models.IntegerField(blank=True, null=True)
    weekflow = models.IntegerField(blank=True, null=True)
    ranks = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    tasteid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'


class Producttype(models.Model):
    producttypeid = models.AutoField(primary_key=True)
    typename = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producttype'


class Recipe(models.Model):
    recipeid = models.AutoField(primary_key=True)
    productid = models.IntegerField(blank=True, null=True)
    ingredientid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
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
    workingstatus = models.CharField(max_length=1, blank=True, null=True)
    rankedstar = models.FloatField(blank=True, null=True)
    weekflow = models.IntegerField(blank=True, null=True)
    monthflow = models.IntegerField(blank=True, null=True)
    deliverytype = models.CharField(max_length=1, blank=True, null=True)
    likesnum = models.IntegerField(blank=True, null=True)
    deliveryfromprice = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'restaurant'


class SearchRecords(models.Model):
    recordid = models.AutoField(primary_key=True)
    userid = models.IntegerField(blank=True, null=True)
    keywordsid = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'search_records'


class Taste(models.Model):
    tasteid = models.AutoField(primary_key=True)
    tastetype = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'taste'


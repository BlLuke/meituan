from django.contrib import admin
from .models import Products, Purse, Shipper, Customer, Address, Account, Discount, Ingredient, Keywords, Order, \
    Orderhistory, Orderlist, Picture, Priority, ProductTastetype, Recipe, Producttype, Restaurant, SearchRecords, Taste

# Register your models here.
admin.site.register(Products)
admin.site.register(Purse)
admin.site.register(Shipper)
admin.site.register(Customer)
admin.site.register(Address)
admin.site.register(Account)
admin.site.register(Discount)
admin.site.register(Ingredient)
admin.site.register(Keywords)
admin.site.register(Order)
admin.site.register(Orderhistory)
admin.site.register(Orderlist)
admin.site.register(Picture)
admin.site.register(Priority)
admin.site.register(ProductTastetype)
admin.site.register(Recipe)
admin.site.register(Producttype)
admin.site.register(Restaurant)
admin.site.register(SearchRecords)
admin.site.register(Taste)


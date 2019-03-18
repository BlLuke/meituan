from django.shortcuts import render

# Create your views here.
from order.models import Account, Customer, Address
from user.forms import customer_form, account_form, restaurant_form


# 显示主页
def homepage_view(request):
    return render(request,"index.html")

# 账户登录：无论customer,restaurant,shipper
def account_login_view(request):
    if request.method == "GET":
        uname = request.GET.get("uname","用户名不存在")
        pswd = request.GET.get("password","")
        account = Account.objects.get(username=uname)
        if account.password == pswd:
            return "登录成功"
        else:
            return render(request,"userlogin.html")

def account_create_view(request):
    if request.method == "POST":
        form = account_form(request.POST)
    else:
        form = account_form()
    if form.is_valid():
        Account.objects.create(**form.cleaned_data)
    context = \
    {
        'form': form
    }
    return render(request,"",context)

def restaurant_create_view(request):
    if request.method =="POST":
        form = restaurant_form(request.POST)
    else:
        form = restaurant_form()
    if form.is_valid():
        Account.objects.create(**form.cleaned_data)
    context = \
    {
        'form': form
    }
    return render(request,"",context)

def customer_create_view(request):
    if request.method =="POST":
        form1 = customer_form(request.POST)
    else:
        form1 = customer_form()
    if form1.is_valid():
        Customer.objects.create(**form1.cleaned_data)
        Address.objects.create(**form1.cleaned_data)
    context = \
    {
        'form': form1
    }
    return render(request,"",context)

def shipper_create_view(requst):
    pass
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

# 动态查找视图
from order.models import Products


def dynamic_lookup_view(request,id):
    try:
        obj = Products.objects.get(id=id)
        print(obj.title)
    except Products.DoesNotExist:
        raise Http404
    return render(request, "/product_detail.html", locals())

# 考虑删除功能添加必要性
def product_delete_view(request,id):
    obj = get_object_or_404(Products, id=id)
    # POST  requirement
    if request.method == "POST":
        obj.delete()
        return redirect("../")
    context = {
        "object": obj
    }
    return render(request, "product_delete.html", context)

def product_create_view(request):
    if request.method == "POST":
        form = rawproductForm(request.POST)
    else:
        form = rawproductForm()
    if form.is_valid():
        print(form.cleaned_data)
        Product.objects.create(**form.cleaned_data)
    context = {
            'form':form
            }
    return render(request, "/templates/product_create.html", context)


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
            'object':obj
            }
    return render(request, "../templates/product_detail.html", context)


def productlist_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list":queryset

    }
    return render(request, "../templates/productlist.html", context)
from django import forms

class account_form(forms.Form):
    password = forms.CharField()
    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    is_active = forms.IntegerField()
    date_joined = forms.DateTimeField()


class customer_form(forms.Form):
    pass

class restaurant_form(forms.Form):
    name = forms.CharField()  # Field name made lowercase.
    gender = forms.IntegerField()  # Field name made lowercase.
    address1 = forms.CharField()
    address2 = forms.CharField()
    address3 = forms.CharField()
    address4 = forms.CharField()
    defaultaddr = forms.IntegerField()
    balance = forms.DecimalField()
    alipayaccount = forms.CharField()
    wechataccount = forms.CharField()
    memership = forms.IntegerField()
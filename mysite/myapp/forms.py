from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import Order, Sale
import calculation


class AddCustomerForm(forms.Form):
    customer_name = forms.CharField(max_length=20)
    l_name = forms.CharField(max_length=20)
    email = forms.EmailField(label='Email', required=False)
    phone = forms.IntegerField(label='Phone')

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class AddSaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['customer_ID', 'item_ID', 'employee_ID', 'quantity', 'total_cost']

        widgets = {'total_cost': calculation.FormulaInput('quantity*item_ID__item_cost')}

class AddOrderFrom(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['item_ID', 'employee_ID', 'quantity', 'order_cost']

        widgets = {'order_cost': calculation.FormulaInput('quantity*item_ID__item_cost')}

    
        
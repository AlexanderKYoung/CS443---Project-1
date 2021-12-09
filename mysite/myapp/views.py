from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.views.generic import ListView, CreateView
from django.contrib import messages
from myapp.models import Sale, Customer, Stock, Manufacturer, Order, Employee
from django import template
from .forms import AddOrderFrom, UserRegisterForm

from .forms import AddCustomerForm, AddSaleForm

from django.db.models import Sum

register = template.Library()

def home(request):
    sales = Sale.objects.all().order_by('-quantity', 'item_ID')
    q_sums = Sale.objects.values('item_ID__item_name', 'item_ID__manuf_ID__manuf_name').annotate(total_quantity=Sum('quantity')).order_by('-total_quantity', 'item_ID')
    args = {'range5': range(1,6), 'sales': sales, 'q_sums': q_sums}
    return render(request, 'myapp/home.html', args)

def pos(request):
    form = AddCustomerForm()
    sale_form = AddSaleForm(request.POST or None)
    sales = Sale.objects.values('item_ID__item_cost', 'item_ID__manuf_ID__manuf_name', 'item_ID__item_name', 'quantity', 'total_cost')
    sales = sales.latest('sale_ID')

    if sale_form.is_valid():
        quantity = sale_form.cleaned_data.get('quantity')
        item_id = sale_form.cleaned_data['item_ID']
        stock = Stock.objects.get(item_name=item_id)
        stock.item_quantity -= quantity
        stock.save()
        sale_form.save()

    args = {
        'stocks': Stock.objects.all().order_by('item_name'),
        'sales': sales,
        'form': form,
        'sale_form': sale_form
    }
    return render(request, 'myapp/point_of_sale.html', args)

def tickets(request):
    args = {
        'sales': Sale.objects.all().order_by('-date')
    }
    return render(request, 'myapp/tickets.html', args)

def orders(request):
    args = {
        'orders': Order.objects.all().order_by('-order_date')
    }
    return render(request, 'myapp/orders.html', args)

def stocks(request):
    args = {
        'stocks': Stock.objects.all()
    }
    return render(request, 'myapp/stocks.html', args)

def order(request):
    form = AddOrderFrom(request.POST or None)
    if form.is_valid():
        quantity = form.cleaned_data.get('quantity')
        item_id = form.cleaned_data['item_ID']
        stock = Stock.objects.get(item_name=item_id)
        stock.item_quantity += quantity
        stock.save()
        form.save()
        return redirect('storefront-home')

    args = {
        'stocks': Stock.objects.all().order_by('item_name'),
        'form': form
    }

    return render(request, 'myapp/order.html', args)

class StockListView(ListView):
    model = Stock
    template_name = 'myapp/point_of_sale.html'
    context_object_name = 'stocks'
    ordering = ['item_name']
    
class CustomerCreateView(CreateView):
    model = Customer
    fields = ['name', 'l_name', 'email', 'phone', 'address']
    def get_success_url(self):
        return reverse('point-of-sale')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('storefront-home')
    else:
        form = UserRegisterForm()
    return render(request, 'myapp/register.html', {'form': form})

def customer_search_view(request):
    return render(request, 'myapp/search-customers.html', {})

class StockCreateView(CreateView):
    model = Stock
    fields = ['manuf_ID', 'item_name', 'item_model', 'item_quantity', 'item_cost']
    def get_success_url(self):
        return reverse('point-of-sale')
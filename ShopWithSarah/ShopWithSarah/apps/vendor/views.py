from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify

from .models import Vendor
from .forms import ProductForm
from apps.product.models import Product
from django.shortcuts import render,redirect

# Create your views here.
def own_shop(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            vendor =Vendor.objects.create(name=user.username, created_by=user)

            return redirect('frontpage')
    
    else:
        form = UserCreationForm()
    return render(request, 'vendor/ownshop.html', {'form': form})

@login_required
def shop_admin(request):
    vendor = request.user.vendor
    products = vendor.products.all()
    return render(request, 'vendor/shop_admin.html', {'vendor': vendor, 'products': products},)

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = request.user.vendor
            product.slug = slugify(product.title)
            product.save()

            return redirect('shop_admin')
    
    else:
        form = ProductForm()
    return render(request, 'vendor/add_product.html', {'form': form})
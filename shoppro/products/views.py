from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from .models import *
from .forms import *
from django.views.generic import UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from django.core.mail import send_mail

from django.conf import settings


class ProductListView(ListView):
    model = TheProduct
    context_object_name = 'products'
    template_name = "view.html"

def home(request):
    up = TheProduct.objects.all()
    context = {'up':up}
    return render(request, 'view.html', context)
    

def deleteview(request):
    obj = TheProduct.objects.all()
    
    context = {
        'products': obj,
    }
    return render(request, 'view.html', context)

class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    template_name = "products/update.html"
    success_url = reverse_lazy('home')


def create_category(request):
    return render(request, 'products/base.html')


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'upload_book.html', {
        'form': form
    })


def products(request):
    form = TheProductForm()
    if request.method == 'POST':
        form = TheProductForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = TheProductForm()
    products = Product.objects.all()
    return render(request, 'products.html', {
        'products': products,
        'form': form
    })


def productFormCreate(request):
    form = TheProductForm(request.POST, request.FILES)
    if request.method == 'POST':
        form = TheProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products:home')
    else:
        form = TheProductForm()
    return render(request, 'products/create.html', {
        'form': form
    })
    
    
def update(request, pk):
    Up_Product = get_object_or_404(TheProduct, pk=pk)
    if request.method == 'POST':
        form = TheProductForm(request.POST, request.FILES, instance=Up_Product)
        if form.is_valid():
            Up_Product = form.save(commit=False)
            Up_Product.save()
            return redirect('products:home')
    else:
        form = TheProductForm(instance=Up_Product)
    return render(request, 'products/editproducts.html', {
        'form': form
    })
    
def showproductdetails(request, pk):
    p = TheProduct.objects.get(pk=pk)
    return render(request, 'products/purchase.html', {
        'p':p
    })


class TheProductDeleteView(DeleteView):
    model = TheProduct
    template_name = "product-delete.html"
    success_url = reverse_lazy('products:home')


def showform(request):
    return render(request, 'showproduct.html')
    

def showlist(request, productname, quantity):
    context = {
        'product':productname,
        'quantity':quantity
    }
    return render(request, 'show_list.html', context)


def upload_product(request):
    return render(request, 'upload_product.html', {})



def SendEmail(request):
    subject = 'Some Email'
    from_email = settings.DEFAULT_FROM_EMAIL
    message = 'This is a test mail'
    receipient_list = ['doikuomola@gmail.com']
    html_message = 'this is  django class'
    
    send_mail(
    subject,
    message,
    from_email,
    receipient_list,
    fail_silently=False,
    html_message=html_message
)
    
from django.urls import path
from products.views import *


app_name = 'products'

urlpatterns = [
    path('create/', productFormCreate, name='create'),
    path('products/', products, name='products'),
    path('books/', book_list, name='book_list'),
    path('books/upload/', upload_book, name='upload_book'),
    path('create_category/', create_category, name='create_category'),
    path('<int:pk>/delete/', TheProductDeleteView.as_view(), name='delete'),
    path('upload-product/', upload_product, name='upload-product'),
    path('', ProductListView.as_view(), name='home'),
    path('sendemail/', SendEmail, name='sendemail'),
    # path('delete/<int:pk>/', delete, name='delete'),
    path('update/<int:pk>/', update, name='update'),
    path('showproductdetails/<int:pk>/', showproductdetails, name='showproductdetails'),
]



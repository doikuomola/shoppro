from django.urls import path, include

from .views import *

app_name = 'accounts'

urlpatterns = [
    # path('create/', productFormCreate, name='create'),
    # path('customerformview/', customerformview, name='customerformview'),
    # path('products/', products, name='products'),
    # path('books/', book_list, name='book_list'),
    # path('books/customer/', customer_form_view, name='customer_form_view'),
    # path('books/upload/', upload_book, name='upload_book'),
    # path('create_category/', create_category, name='create_category'),
    # path('login/', login_view, name='login'),
    # path('delete/<init>:pk/', TheProductDeleteView.as_view(), name='delete'),
    # path('dotest2/<str:mystring>/<int:quantity>', showform, name='dotest2'),
    # path('dotest3/', showlist, name='dotest3'),
    # path('', view, name='home'),
    # path('register/', register, name='register'),
    # path('<int:pk>/edit/', ProductUpdateView.as_view(), name='edit'),
    # path('create/', create, name='create'),
    path('register/', register, name='register'),

]



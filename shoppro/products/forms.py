from django import forms
from .models import UserModel, Book, Product, TheProduct
from django.forms import ModelChoiceField


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = '__all__'


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title','author','pdf')

# class ProductCreate(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = '__all__'


# class CustomerForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = Customer
#         fields = ('name', 'email', 'password', 'instrument_purchase', 'house_no', 'address_line1', 'address_line2', 'telephone', 'zip_code', 'state', 'country')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class TheProductForm(forms.ModelForm):
    class Meta:
        model = TheProduct
        fields = "__all__"

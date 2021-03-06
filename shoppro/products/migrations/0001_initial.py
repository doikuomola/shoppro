# Generated by Django 3.2 on 2021-05-25 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('pdf', models.FileField(upload_to='books/pdfs/')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('instrument_purchase', models.CharField(max_length=100)),
                ('house_no', models.CharField(max_length=100)),
                ('address_line1', models.CharField(max_length=100)),
                ('address_line2', models.CharField(max_length=100)),
                ('telephone', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50, unique=True)),
                ('product_quantity', models.CharField(max_length=50)),
                ('product_image', models.ImageField(upload_to='product_name')),
                ('price', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TheProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='Name')),
                ('category', models.CharField(choices=[('Pastries', 'Pastries'), ('Beverages', 'Beverages'), ('Wine', 'Wine'), ('Detergents', 'Detergents')], max_length=20, verbose_name='Select Category')),
                ('image', models.ImageField(upload_to='product_image')),
                ('unit_price', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=30)),
                ('img', models.FileField(upload_to='images/')),
            ],
        ),
    ]

# Generated by Django 3.2 on 2021-05-27 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_theproduct_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theproduct',
            name='quantity',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
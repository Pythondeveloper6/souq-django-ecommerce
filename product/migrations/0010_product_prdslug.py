# Generated by Django 2.1.4 on 2019-09-28 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_product_prdimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='PRDSLug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]

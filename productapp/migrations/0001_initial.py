# Generated by Django 4.2.4 on 2023-08-15 04:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('image', models.ImageField(blank=True, upload_to='brand')),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('image', models.ImageField(blank=True, upload_to='category')),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True, max_length=500)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('original_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('selling_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('image', models.ImageField(blank=True, upload_to='product')),
                ('quantity', models.IntegerField()),
                ('available', models.BooleanField(default=True)),
                ('created_date', models.DateField(auto_now=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('image1', models.ImageField(blank=True, upload_to='product1')),
                ('image2', models.ImageField(blank=True, upload_to='product2')),
                ('image3', models.ImageField(blank=True, upload_to='product3')),
                ('active', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='productapp.brand')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='productapp.category')),
                ('sub', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='productapp.subcategory')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'ordering': ('name',),
            },
        ),
    ]

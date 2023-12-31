# Generated by Django 4.2.4 on 2023-10-11 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0006_remove_brand_slug_remove_category_slug_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='bannerImage')),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]

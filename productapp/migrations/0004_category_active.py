# Generated by Django 4.2.4 on 2023-08-15 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0003_alter_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]

# Generated by Django 4.2.4 on 2023-10-13 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0022_delete_invoice'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='return_requested',
            field=models.BooleanField(default=False),
        ),
    ]
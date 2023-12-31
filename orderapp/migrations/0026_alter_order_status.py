# Generated by Django 4.2.4 on 2023-10-13 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0025_remove_order_return_requested'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Confirmed', 'Confirmed'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered'), ('Ready to Deliver', 'Ready to Deliver'), ('Cancelled', 'Cancelled'), ('Return Requested', 'Return Requested'), ('Return Request Rejected', 'Return Requested Rejected'), ('Returned', 'Returned')], default='Confirmed', max_length=30),
        ),
    ]

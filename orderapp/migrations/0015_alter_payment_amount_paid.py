# Generated by Django 4.2.4 on 2023-10-05 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0014_order_used_coupon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='amount_paid',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]

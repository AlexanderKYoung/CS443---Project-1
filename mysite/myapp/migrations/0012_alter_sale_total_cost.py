# Generated by Django 3.2.9 on 2021-11-21 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_alter_order_order_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='total_cost',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]

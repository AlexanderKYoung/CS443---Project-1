# Generated by Django 3.2.9 on 2021-11-20 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_rename_item_id_sale_item_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='item_name',
            new_name='item_ID',
        ),
    ]

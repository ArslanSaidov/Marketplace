# Generated by Django 4.1.3 on 2023-05-19 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0012_remove_product_brand_delete_brand'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='nineshnaya_cena',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='proshlaya_cena',
        ),
    ]

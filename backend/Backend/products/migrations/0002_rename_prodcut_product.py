# Generated by Django 4.0.4 on 2023-09-03 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Prodcut',
            new_name='Product',
        ),
    ]
# Generated by Django 4.2.6 on 2024-02-08 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='frst_name',
            new_name='first_name',
        ),
    ]

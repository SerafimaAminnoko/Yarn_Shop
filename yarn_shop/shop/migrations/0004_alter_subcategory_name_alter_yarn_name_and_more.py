# Generated by Django 4.2.6 on 2023-11-09 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_yarnimages_yarn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='yarn',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='yarnimages',
            name='title',
            field=models.CharField(max_length=40),
        ),
    ]

# Generated by Django 3.2.6 on 2021-09-27 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20210927_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='name',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]

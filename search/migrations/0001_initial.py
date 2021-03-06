# Generated by Django 3.2.6 on 2021-09-22 13:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.CharField(max_length=13, unique=True)),
                ('name', models.CharField(max_length=45, unique=True)),
                ('brands', models.CharField(max_length=45)),
                ('url', models.URLField()),
                ('url_image', models.URLField()),
                ('url_image_small', models.URLField()),
                ('nutrition_score', models.CharField(max_length=1)),
                ('energy_100g', models.FloatField(default=0, null=True)),
                ('sugars_100g', models.FloatField(default=0, null=True)),
                ('sodium_100g', models.FloatField(default=0, null=True)),
                ('fat_100g', models.FloatField(default=0, null=True)),
                ('salt_100g', models.FloatField(default=0, null=True)),
                ('category', models.ManyToManyField(to='search.Categories')),
            ],
        ),
        migrations.CreateModel(
            name='Substitute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_product', to='search.product')),
                ('substitute_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_substitute', to='search.product')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 4.2.20 on 2025-05-14 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_remove_piercing_precio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='piercing',
            name='precio',
            field=models.IntegerField(default=250),
        ),
    ]

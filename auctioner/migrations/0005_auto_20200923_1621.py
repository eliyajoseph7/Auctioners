# Generated by Django 3.1 on 2020-09-23 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctioner', '0004_auto_20200922_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]

# Generated by Django 3.2 on 2021-05-19 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_remove_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproduct',
            name='expectedDelivery',
            field=models.DateField(blank=True, default='2099/05/31'),
        ),
    ]

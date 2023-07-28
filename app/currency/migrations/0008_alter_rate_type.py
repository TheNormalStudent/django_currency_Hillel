# Generated by Django 4.2.3 on 2023-07-28 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0007_responselog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='type',
            field=models.CharField(choices=[('USD', 'US Dollar'), ('EUR', 'Euro')], max_length=3),
        ),
    ]

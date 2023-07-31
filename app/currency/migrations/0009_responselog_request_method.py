# Generated by Django 4.2.3 on 2023-07-29 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0008_alter_rate_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='responselog',
            name='request_method',
            field=models.CharField(choices=[('GET', 'get'), ('POST', 'post')], default='', max_length=8),
            preserve_default=False,
        ),
    ]
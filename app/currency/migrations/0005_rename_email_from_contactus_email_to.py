# Generated by Django 4.2.3 on 2023-07-21 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0004_contactus_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='email_from',
            new_name='email_to',
        ),
    ]
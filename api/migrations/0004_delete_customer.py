# Generated by Django 3.0.8 on 2022-04-12 02:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20220412_0306'),
        ('api', '0003_customer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
    ]

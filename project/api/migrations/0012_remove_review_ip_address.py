# Generated by Django 3.0.2 on 2020-01-29 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20200129_0543'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='ip_address',
        ),
    ]

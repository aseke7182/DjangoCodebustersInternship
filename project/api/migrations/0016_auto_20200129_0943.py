# Generated by Django 3.0.2 on 2020-01-29 09:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20200129_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='submission_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

# Generated by Django 3.0.3 on 2020-04-04 09:03

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200404_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 4, 9, 3, 2, 138755, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

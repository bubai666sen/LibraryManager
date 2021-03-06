# Generated by Django 2.2.2 on 2019-12-25 17:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0002_auto_20191225_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 25, 17, 5, 38, 629187, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='book',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 25, 17, 5, 38, 629187, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='booktransaction',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 25, 17, 5, 38, 631180, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='booktransaction',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 25, 17, 5, 38, 631180, tzinfo=utc)),
        ),
    ]

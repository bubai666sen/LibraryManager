# Generated by Django 2.2.2 on 2019-12-26 16:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0003_auto_20191225_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 26, 16, 52, 20, 818994, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='book',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 26, 16, 52, 20, 818994, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='booktransaction',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 26, 16, 52, 20, 819948, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='booktransaction',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 26, 16, 52, 20, 819948, tzinfo=utc)),
        ),
    ]

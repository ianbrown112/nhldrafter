# Generated by Django 2.0.2 on 2018-02-10 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_auto_20180210_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='shots',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 2.0.2 on 2018-03-07 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='squad',
            name='draft_order',
            field=models.IntegerField(default=0),
        ),
    ]

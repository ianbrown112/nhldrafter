# Generated by Django 2.0.2 on 2018-03-10 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0003_league_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='league',
            name='goalie_amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='league',
            name='skater_amount',
            field=models.IntegerField(default=0),
        ),
    ]

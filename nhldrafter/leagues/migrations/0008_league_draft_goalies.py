# Generated by Django 2.0.2 on 2018-03-18 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0007_league_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='league',
            name='draft_goalies',
            field=models.BooleanField(default=True),
        ),
    ]

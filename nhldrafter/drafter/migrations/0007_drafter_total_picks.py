# Generated by Django 2.0.2 on 2018-03-18 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drafter', '0006_remove_drafter_draft_goalies'),
    ]

    operations = [
        migrations.AddField(
            model_name='drafter',
            name='total_picks',
            field=models.IntegerField(default=0),
        ),
    ]
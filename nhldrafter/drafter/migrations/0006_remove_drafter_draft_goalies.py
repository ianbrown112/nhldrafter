# Generated by Django 2.0.2 on 2018-03-18 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drafter', '0005_auto_20180318_1736'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drafter',
            name='draft_goalies',
        ),
    ]
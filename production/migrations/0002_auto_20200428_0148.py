# Generated by Django 2.2.4 on 2020-04-27 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prediction',
            name='commod',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='prediction',
            name='idn',
            field=models.IntegerField(default=0),
        ),
    ]

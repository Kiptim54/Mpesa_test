# Generated by Django 2.0 on 2018-08-07 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpesa', '0010_auto_20180807_0756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
        migrations.AddField(
            model_name='profile',
            name='Account_Balance',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.0 on 2018-08-07 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpesa', '0003_auto_20180807_0553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Account_Balance',
            field=models.IntegerField(null=True),
        ),
    ]

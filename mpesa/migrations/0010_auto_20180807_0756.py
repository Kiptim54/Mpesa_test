# Generated by Django 2.0 on 2018-08-07 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpesa', '0009_auto_20180807_0753'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='birth_date',
        ),
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

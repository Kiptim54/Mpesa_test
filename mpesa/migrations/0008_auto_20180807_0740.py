# Generated by Django 2.0 on 2018-08-07 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpesa', '0007_auto_20180807_0647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='Account_Balance',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]

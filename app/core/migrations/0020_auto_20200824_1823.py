# Generated by Django 2.1.15 on 2020-08-24 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20200824_1710'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wxstatreading',
            old_name='loc',
            new_name='LocationID',
        ),
        migrations.RenameField(
            model_name='wxstatreading',
            old_name='device',
            new_name='deviceID',
        ),
        migrations.RemoveField(
            model_name='wxstatreading',
            name='user',
        ),
        migrations.AddField(
            model_name='wxstatreading',
            name='LocationDescription',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='wxstatreading',
            name='SystemType',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='wxstatreading',
            name='solar_rad',
            field=models.FloatField(null=True),
        ),
    ]

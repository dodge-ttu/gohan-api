# Generated by Django 2.1.15 on 2020-08-24 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20200821_1816'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tankmonitorreading',
            old_name='loc',
            new_name='LocationID',
        ),
        migrations.RenameField(
            model_name='tankmonitorreading',
            old_name='rainfall_mm',
            new_name='RainFallMillimeters',
        ),
        migrations.RenameField(
            model_name='tankmonitorreading',
            old_name='water_height_mm',
            new_name='WaterHeightMillimeters',
        ),
        migrations.RenameField(
            model_name='tankmonitorreading',
            old_name='device',
            new_name='deviceID',
        ),
        migrations.RemoveField(
            model_name='tankmonitorreading',
            name='user',
        ),
        migrations.AddField(
            model_name='tankmonitorreading',
            name='LocationDescription',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tankmonitorreading',
            name='SystemType',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
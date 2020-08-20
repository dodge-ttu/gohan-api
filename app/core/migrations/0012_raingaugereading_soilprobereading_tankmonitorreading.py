# Generated by Django 2.1.15 on 2020-08-20 21:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20200820_1904'),
    ]

    operations = [
        migrations.CreateModel(
            name='Raingaugereading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(null=True)),
                ('rain', models.FloatField(null=True)),
                ('accum_rain', models.FloatField(null=True)),
                ('device', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Device')),
                ('loc', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Location')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Soilprobereading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Device')),
                ('loc', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Location')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tankmonitorreading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(null=True)),
                ('water_height_mm', models.FloatField(null=True)),
                ('rainfall_mm', models.FloatField(null=True)),
                ('device', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Device')),
                ('loc', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Location')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

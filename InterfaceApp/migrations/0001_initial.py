# Generated by Django 4.1.1 on 2022-10-12 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PerformanceList',
            fields=[
                ('seq', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('startDate', models.IntegerField()),
                ('endDate', models.IntegerField()),
                ('place', models.CharField(max_length=50)),
                ('realmName', models.CharField(max_length=10)),
                ('area', models.CharField(max_length=10, null=True)),
                ('thumbnail', models.CharField(max_length=256)),
                ('gpsX', models.FloatField(null=True)),
                ('gpsY', models.FloatField(null=True)),
            ],
        ),
    ]

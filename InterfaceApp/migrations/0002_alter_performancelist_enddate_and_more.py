# Generated by Django 4.1.1 on 2022-10-12 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InterfaceApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performancelist',
            name='endDate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='performancelist',
            name='startDate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='performancelist',
            name='thumbnail',
            field=models.BinaryField(),
        ),
    ]

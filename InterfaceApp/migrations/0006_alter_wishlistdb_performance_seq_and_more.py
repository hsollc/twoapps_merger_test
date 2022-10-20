# Generated by Django 4.1.1 on 2022-10-20 11:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('InterfaceApp', '0005_wishlistdb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlistdb',
            name='performance_seq',
            field=models.ForeignKey(db_column='performance_seq', on_delete=django.db.models.deletion.CASCADE, to='InterfaceApp.performancedb'),
        ),
        migrations.AlterField(
            model_name='wishlistdb',
            name='user_id',
            field=models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

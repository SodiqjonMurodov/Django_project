# Generated by Django 3.1.14 on 2022-07-08 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='created',
            field=models.DateField(auto_now=True),
        ),
    ]
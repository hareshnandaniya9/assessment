# Generated by Django 4.1.3 on 2022-11-08 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='mobile',
            field=models.CharField(max_length=100),
        ),
    ]

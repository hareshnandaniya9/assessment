# Generated by Django 4.1.3 on 2022-11-08 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_feedback_mobile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='remarks',
            new_name='feedback',
        ),
    ]

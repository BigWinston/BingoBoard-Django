# Generated by Django 4.0.3 on 2022-03-13 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_staff_is_active_remove_staff_is_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='password',
        ),
    ]

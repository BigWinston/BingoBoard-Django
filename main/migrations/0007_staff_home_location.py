# Generated by Django 4.0.3 on 2022-03-13 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='home_location',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.location'),
            preserve_default=False,
        ),
    ]

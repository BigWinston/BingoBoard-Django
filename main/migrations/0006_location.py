# Generated by Django 4.0.3 on 2022-03-13 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_staff_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abbrev', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
    ]

# Generated by Django 2.2.3 on 2020-07-23 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfile', '0004_auto_20200723_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]

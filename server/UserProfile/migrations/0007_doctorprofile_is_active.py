# Generated by Django 2.2.3 on 2020-07-23 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfile', '0006_auto_20200723_2356'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorprofile',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
# Generated by Django 2.0.5 on 2018-06-09 01:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('computermonitor', '0005_auto_20180608_0216'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='computerbackup',
            options={'get_latest_by': 'backup_time'},
        ),
    ]
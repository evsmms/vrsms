# Generated by Django 3.2.5 on 2022-06-29 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20220629_1237'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='serviceschedule',
            options={'verbose_name': 'Service Schedule', 'verbose_name_plural': 'Service Schedules'},
        ),
        migrations.RemoveField(
            model_name='serviceschedule',
            name='ref',
        ),
        migrations.AddField(
            model_name='serviceschedule',
            name='schedule_name',
            field=models.CharField(default='', max_length=100, verbose_name='Schedule Name'),
            preserve_default=False,
        ),
    ]

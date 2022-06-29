# Generated by Django 3.2.5 on 2022-06-29 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repairs', '0002_auto_20220602_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repairticket',
            name='frequency',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='frequency'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='cost',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Title'),
        ),
    ]

# Generated by Django 3.2.5 on 2022-05-26 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repairs', '0002_auto_20220526_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='ref_no',
            field=models.CharField(default='81D5A', editable=False, max_length=50, primary_key=True, serialize=False),
        ),
    ]

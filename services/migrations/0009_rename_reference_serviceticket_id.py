# Generated by Django 3.2.5 on 2022-05-26 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_alter_serviceticket_reference'),
    ]

    operations = [
        migrations.RenameField(
            model_name='serviceticket',
            old_name='reference',
            new_name='id',
        ),
    ]

# Generated by Django 3.2.5 on 2022-06-01 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repairs', '0007_alter_ticket_ref_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='ref_no',
            field=models.CharField(default='81456', editable=False, max_length=50, primary_key=True, serialize=False),
        ),
    ]

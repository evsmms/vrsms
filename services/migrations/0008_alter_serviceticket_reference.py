# Generated by Django 3.2.5 on 2022-05-26 20:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_alter_serviceticket_ref_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceticket',
            name='reference',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]

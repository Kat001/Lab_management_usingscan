# Generated by Django 3.0.4 on 2020-05-23 11:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('PCT', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='v_id',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]

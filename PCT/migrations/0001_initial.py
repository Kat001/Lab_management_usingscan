# Generated by Django 3.0.4 on 2020-05-23 11:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('v_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('v_name', models.CharField(max_length=50)),
                ('v_address', models.CharField(max_length=400)),
                ('v_mob', models.CharField(max_length=10, unique=True)),
                ('join_date', models.DateField(auto_now_add=True)),
                ('v_image', models.ImageField(default='default.jpg', upload_to='')),
            ],
        ),
    ]

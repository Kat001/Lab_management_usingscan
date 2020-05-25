# Generated by Django 3.0.4 on 2020-05-23 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PCT', '0002_auto_20200523_1638'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lab4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastvisit_date', models.DateField(auto_now_add=True)),
                ('visit_no', models.IntegerField(default=0)),
                ('v_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PCT.Volunteer')),
            ],
        ),
        migrations.CreateModel(
            name='Lab3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastvisit_date', models.DateField(auto_now_add=True)),
                ('visit_no', models.IntegerField(default=0)),
                ('v_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PCT.Volunteer')),
            ],
        ),
        migrations.CreateModel(
            name='Lab2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastvisit_date', models.DateField(auto_now_add=True)),
                ('visit_no', models.IntegerField(default=0)),
                ('v_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PCT.Volunteer')),
            ],
        ),
        migrations.CreateModel(
            name='Lab1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastvisit_date', models.DateField(auto_now_add=True)),
                ('visit_no', models.IntegerField(default=0)),
                ('v_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PCT.Volunteer')),
            ],
        ),
    ]

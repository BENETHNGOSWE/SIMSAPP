# Generated by Django 4.2.1 on 2023-06-03 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simsapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='module',
        ),
        migrations.AddField(
            model_name='student',
            name='module',
            field=models.ManyToManyField(blank=True, null=True, to='simsapp.module'),
        ),
    ]

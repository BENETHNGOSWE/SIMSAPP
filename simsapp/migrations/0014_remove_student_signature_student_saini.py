# Generated by Django 4.2.1 on 2023-05-29 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simsapp', '0013_remove_student_saini_student_signature'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='signature',
        ),
        migrations.AddField(
            model_name='student',
            name='saini',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
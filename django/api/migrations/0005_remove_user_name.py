# Generated by Django 4.2.7 on 2024-01-15 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_workout_exercise'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
    ]

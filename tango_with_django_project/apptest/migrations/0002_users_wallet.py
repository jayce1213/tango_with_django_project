# Generated by Django 2.1.5 on 2024-03-01 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='wallet',
            field=models.IntegerField(default=0),
        ),
    ]

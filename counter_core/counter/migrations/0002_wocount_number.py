# Generated by Django 2.1.4 on 2018-12-16 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wocount',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]
# Generated by Django 3.1 on 2021-01-16 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20210113_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.URLField(max_length=400),
        ),
    ]
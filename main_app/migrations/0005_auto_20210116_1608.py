# Generated by Django 3.1 on 2021-01-16 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20210116_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='points',
            field=models.IntegerField(default='1000'),
        ),
    ]

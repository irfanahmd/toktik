# Generated by Django 3.1 on 2021-01-18 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_auto_20210118_0228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.CharField(choices=[('SCIENCE', 'SCI'), ('MATHEMATICS', 'MAT'), ('GARDEN', 'GAR'), ('OTHER', 'OTH')], max_length=24),
        ),
    ]

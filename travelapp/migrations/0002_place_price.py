# Generated by Django 4.1.4 on 2022-12-31 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='price',
            field=models.IntegerField(default='0'),
            preserve_default=False,
        ),
    ]

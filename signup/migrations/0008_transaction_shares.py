# Generated by Django 2.2.6 on 2019-12-10 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0007_auto_20191121_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='shares',
            field=models.IntegerField(default=None, verbose_name=1000),
            preserve_default=False,
        ),
    ]

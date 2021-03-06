# Generated by Django 2.2.6 on 2019-11-14 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='signup',
            fields=[
                ('username', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=8)),
                ('phoneno', models.BigIntegerField(max_length=10)),
                ('city', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='stocks',
            fields=[
                ('symbol', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=23)),
                ('last', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('change', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('change_percentage', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
            ],
        ),
    ]

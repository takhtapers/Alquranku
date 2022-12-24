# Generated by Django 4.1.4 on 2022-12-19 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_alquran'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doa',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('doa', models.CharField(max_length=100)),
                ('ayat', models.CharField(max_length=1000)),
                ('latin', models.TextField()),
                ('artinya', models.TextField()),
            ],
        ),
    ]

# Generated by Django 4.1.4 on 2022-12-19 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alquran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arti', models.CharField(max_length=1000)),
                ('asma', models.CharField(max_length=1000)),
                ('audio', models.FileField(upload_to='')),
                ('ayat', models.IntegerField()),
                ('keterangan', models.TextField()),
                ('nama', models.CharField(max_length=1000)),
                ('nomor', models.IntegerField()),
                ('rukuk', models.IntegerField()),
                ('urut', models.IntegerField()),
            ],
        ),
    ]

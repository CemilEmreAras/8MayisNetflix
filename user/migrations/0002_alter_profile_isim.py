# Generated by Django 4.1.1 on 2023-08-16 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='isim',
            field=models.CharField(max_length=50, verbose_name='İsminizi Giriniz'),
        ),
    ]

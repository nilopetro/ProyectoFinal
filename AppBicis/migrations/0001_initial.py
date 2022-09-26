# Generated by Django 4.1 on 2022-09-26 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BiciCambiar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bici', models.CharField(max_length=40)),
                ('tipo', models.CharField(max_length=25)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BiciVender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bici', models.CharField(max_length=40)),
                ('tipo', models.CharField(max_length=25)),
                ('precio', models.IntegerField()),
                ('vendEmail', models.EmailField(max_length=254)),
                ('vendTel', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DatosVend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('edad', models.IntegerField()),
                ('direccion', models.CharField(max_length=80)),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.IntegerField()),
            ],
        ),
    ]

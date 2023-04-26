# Generated by Django 4.1.7 on 2023-04-26 19:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('cuerpo_texto', models.TextField()),
                ('fecha_ublicado', models.DateField(default=datetime.date.today)),
                ('reiting', models.IntegerField(default=5)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.autor')),
            ],
        ),
    ]

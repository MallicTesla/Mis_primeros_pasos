# Generated by Django 4.1.7 on 2023-05-01 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publicasion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linia', models.CharField(max_length=100)),
                ('publicasiones', models.ManyToManyField(to='munchosamunchos.publicasion')),
            ],
        ),
    ]

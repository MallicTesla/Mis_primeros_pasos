# Generated by Django 4.1.7 on 2023-04-07 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_rename_first_name_director_apellido_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pelicula',
            old_name='autor',
            new_name='director',
        ),
    ]

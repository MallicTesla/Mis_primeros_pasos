# Generated by Django 4.1.7 on 2023-04-07 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='director',
            old_name='first_name',
            new_name='apellido',
        ),
        migrations.RenameField(
            model_name='director',
            old_name='date_of_birth',
            new_name='fecha_defuncion',
        ),
        migrations.RenameField(
            model_name='director',
            old_name='date_of_death',
            new_name='fecha_nacimiento',
        ),
        migrations.RenameField(
            model_name='director',
            old_name='last_name',
            new_name='primer_nombre',
        ),
    ]
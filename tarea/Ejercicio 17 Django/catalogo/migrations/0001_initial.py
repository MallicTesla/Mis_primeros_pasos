# Generated by Django 4.1.7 on 2023-04-07 17:52

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('date_of_death', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='nombre del genero', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=32)),
                ('resumen', models.TextField(help_text='Brebe descripsin de la pelicula', max_length=100)),
                ('isbn', models.CharField(help_text='el ISBN de 13 caracteres', max_length=13, verbose_name='ISBN')),
                ('autor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogo.director')),
                ('genero', models.ManyToManyField(to='catalogo.genero')),
            ],
        ),
        migrations.CreateModel(
            name='Instancia_pelicula',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='ide unico para este libro', primary_key=True, serialize=False)),
                ('imprint', models.CharField(max_length=200)),
                ('estado_de_la_pelicula', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('M', 'Mantenimiento'), ('P', 'Prestado'), ('D', 'Disponible'), ('R', 'Reservado')], default='M', help_text='Disponibilidad del pelicula', max_length=1)),
                ('pelicula', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogo.pelicula')),
            ],
        ),
    ]

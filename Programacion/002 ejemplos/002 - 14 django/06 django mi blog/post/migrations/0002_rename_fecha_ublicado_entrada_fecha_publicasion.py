# Generated by Django 4.1.7 on 2023-04-26 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entrada',
            old_name='fecha_ublicado',
            new_name='fecha_publicasion',
        ),
    ]
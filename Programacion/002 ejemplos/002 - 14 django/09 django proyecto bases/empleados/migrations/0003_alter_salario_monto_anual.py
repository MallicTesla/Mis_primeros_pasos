# Generated by Django 4.1.7 on 2023-05-11 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0002_alter_salario_monto_anual'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salario',
            name='monto_anual',
            field=models.IntegerField(default=10000, max_length=10),
        ),
    ]

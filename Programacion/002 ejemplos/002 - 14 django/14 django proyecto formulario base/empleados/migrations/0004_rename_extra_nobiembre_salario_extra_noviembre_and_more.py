# Generated by Django 4.1.7 on 2023-06-13 23:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0003_alter_empleado_direccion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salario',
            old_name='extra_nobiembre',
            new_name='extra_noviembre',
        ),
        migrations.RenameField(
            model_name='trabajo',
            old_name='descripsion',
            new_name='descripcion',
        ),
        migrations.RemoveField(
            model_name='departamento',
            name='local',
        ),
        migrations.RemoveField(
            model_name='local',
            name='empleado',
        ),
        migrations.RemoveField(
            model_name='pais',
            name='departamento',
        ),
        migrations.RemoveField(
            model_name='salario',
            name='trabajo',
        ),
        migrations.RemoveField(
            model_name='trabajo',
            name='empleado',
        ),
        migrations.AddField(
            model_name='departamento',
            name='pais',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='empleados.pais'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='local',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='empleados.local'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='trabajo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='empleados.trabajo'),
        ),
        migrations.AddField(
            model_name='local',
            name='departamento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='empleados.departamento'),
        ),
        migrations.AddField(
            model_name='trabajo',
            name='salario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='empleados.salario'),
        ),
    ]

# Generated by Django 4.1.7 on 2023-04-20 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='fecha',
            field=models.DateField(null=True),
        ),
    ]

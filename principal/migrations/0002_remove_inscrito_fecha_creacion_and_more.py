# Generated by Django 5.1 on 2024-12-21 17:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inscrito',
            name='fecha_creacion',
        ),
        migrations.RemoveField(
            model_name='institucion',
            name='fecha_creacion',
        ),
        migrations.AddField(
            model_name='inscrito',
            name='institucion_asociada',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='principal.institucion'),
        ),
        migrations.AlterField(
            model_name='inscrito',
            name='correo',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='inscrito',
            name='nombre',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='inscrito',
            name='telefono',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='institucion',
            name='correo_institucion',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='institucion',
            name='nombre_institucion',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='institucion',
            name='telefono_institucion',
            field=models.CharField(max_length=20),
        ),
    ]
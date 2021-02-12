# Generated by Django 2.1.2 on 2018-11-18 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreCliente', models.CharField(max_length=100)),
                ('Direccion', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=100)),
                ('comuna', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=9)),
                ('Email', models.EmailField(max_length=100)),
                ('Idtecnico', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='orden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreCliente', models.CharField(max_length=100)),
                ('FechaHoy', models.DateField()),
                ('HoraInicio', models.TimeField()),
                ('HoraTermino', models.TimeField()),
                ('IDascensor', models.CharField(max_length=3)),
                ('Modelo', models.CharField(max_length=100)),
                ('NombreTecnico', models.CharField(max_length=100)),
                ('Fallas', models.TextField(max_length=1000)),
                ('Reparaciones', models.TextField(max_length=1000)),
                ('PiezasCambiadas', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='tecnico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Idtecnico', models.CharField(max_length=3)),
                ('NombreTecnico', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=100)),
                ('Clave', models.CharField(max_length=20)),
            ],
        ),
    ]

# Generated by Django 2.1.2 on 2018-12-09 03:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0006_auto_20181119_0019'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='Idtecnico',
            new_name='TecnicoAsignado',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='telefono',
            new_name='Telefono',
        ),
        migrations.RenameField(
            model_name='orden',
            old_name='IDascensor',
            new_name='IDAscensor',
        ),
        migrations.RenameField(
            model_name='orden',
            old_name='NombreTecnico',
            new_name='TecnicoAsignado',
        ),
    ]

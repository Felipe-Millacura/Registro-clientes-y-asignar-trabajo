# Generated by Django 2.1.2 on 2018-12-10 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0007_auto_20181209_0049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='ciudad',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='comuna',
        ),
        migrations.AddField(
            model_name='cliente',
            name='Ciudad',
            field=models.CharField(default='Seleccionar Ciudad', max_length=200),
        ),
        migrations.AddField(
            model_name='cliente',
            name='Comuna',
            field=models.CharField(default='Seleccionar Comuna', max_length=200),
        ),
    ]
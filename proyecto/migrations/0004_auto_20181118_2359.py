# Generated by Django 2.1.2 on 2018-11-19 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0003_delete_perrito'),
    ]

    operations = [
        migrations.DeleteModel(
            name='cliente',
        ),
        migrations.DeleteModel(
            name='orden',
        ),
    ]

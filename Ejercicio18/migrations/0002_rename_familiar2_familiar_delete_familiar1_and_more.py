# Generated by Django 4.1 on 2022-08-29 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ejercicio18', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Familiar2',
            new_name='Familiar',
        ),
        migrations.DeleteModel(
            name='Familiar1',
        ),
        migrations.DeleteModel(
            name='Familiar3',
        ),
    ]

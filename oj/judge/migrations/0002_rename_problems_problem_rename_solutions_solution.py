# Generated by Django 4.2.2 on 2023-07-01 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Problems',
            new_name='Problem',
        ),
        migrations.RenameModel(
            old_name='Solutions',
            new_name='Solution',
        ),
    ]
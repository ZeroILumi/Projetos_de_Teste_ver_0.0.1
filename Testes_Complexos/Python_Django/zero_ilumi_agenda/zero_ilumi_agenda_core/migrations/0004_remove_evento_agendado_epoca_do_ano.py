# Generated by Django 3.2.8 on 2021-10-19 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zero_ilumi_agenda_core', '0003_evento_agendado_epoca_do_ano'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento_agendado',
            name='epoca_do_ano',
        ),
    ]

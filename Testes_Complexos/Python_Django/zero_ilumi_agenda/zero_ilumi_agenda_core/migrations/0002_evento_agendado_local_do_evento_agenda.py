# Generated by Django 3.2.8 on 2021-10-16 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zero_ilumi_agenda_core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento_agendado',
            name='local_do_evento_agenda',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Local do Evento'),
        ),
    ]

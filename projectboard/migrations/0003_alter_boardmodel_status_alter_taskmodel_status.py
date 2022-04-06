# Generated by Django 4.0.3 on 2022-04-05 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectboard', '0002_alter_boardmodel_status_alter_taskmodel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardmodel',
            name='status',
            field=models.CharField(choices=[('open', 'open'), ('inprogress', 'inprogress'), ('closed', 'closed')], default='OPEN', max_length=15),
        ),
        migrations.AlterField(
            model_name='taskmodel',
            name='status',
            field=models.CharField(choices=[('open', 'open'), ('inprogress', 'inprogress'), ('complete', 'complete')], default='OPEN', max_length=15),
        ),
    ]
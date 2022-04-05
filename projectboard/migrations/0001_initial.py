# Generated by Django 4.0.3 on 2022-04-05 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teams', '0003_alter_team_members'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, unique=True)),
                ('description', models.CharField(max_length=128)),
                ('creationtime', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('OPEN', 'OPEN'), ('IN_PROGRESS', 'IN_PROGRESS'), ('COMPLETE', 'COMPLETE')], max_length=15)),
                ('user_id', models.ForeignKey(help_text='Select the team for the task', on_delete=django.db.models.deletion.CASCADE, to='teams.team')),
            ],
        ),
        migrations.CreateModel(
            name='Boardmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('description', models.CharField(max_length=128)),
                ('creationtime', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('OPEN', 'OPEN'), ('IN_PROGRESS', 'IN_PROGRESS'), ('COMPLETE', 'COMPLETE')], max_length=15)),
                ('team', models.ForeignKey(help_text='Select team for this project', on_delete=django.db.models.deletion.CASCADE, to='teams.team')),
            ],
        ),
    ]

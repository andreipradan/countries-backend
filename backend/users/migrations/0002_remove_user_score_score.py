# Generated by Django 4.1 on 2022-09-16 13:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='score',
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('score', models.IntegerField(default=0)),
                ('game_type', models.IntegerField(choices=[(1, 'World'), (2, 'North America'), (3, 'South America'), (4, 'Europe'), (5, 'Africa'), (6, 'Asia'), (7, 'Oceania')], default=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scores', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 5.0.7 on 2024-08-06 20:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Textos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_vista', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Parrafos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=200, null=True)),
                ('posicion', models.IntegerField(blank=True, null=True)),
                ('texto', models.TextField(blank=True, null=True)),
                ('vista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.textos')),
            ],
        ),
    ]
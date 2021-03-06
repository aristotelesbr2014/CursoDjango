# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 15:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('utils', '0003_auto_20170129_1520'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fabricante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=32, unique=True)),
                ('endereco', models.CharField(max_length=1024, unique=True)),
                ('cnpj', models.CharField(max_length=14, unique=True)),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utils.Cidade')),
            ],
            options={
                'verbose_name': 'Fabricante',
                'verbose_name_plural': 'Fabricantes',
            },
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=32, unique=True)),
                ('fabricante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.Fabricante')),
            ],
            options={
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marcas',
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=32, unique=True)),
                ('cod', models.CharField(max_length=64, unique=True)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.Marca')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
    ]

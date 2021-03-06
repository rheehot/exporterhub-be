# Generated by Django 3.1.3 on 2020-11-23 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Exporter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('logo_url', models.URLField(max_length=2000)),
                ('stars', models.IntegerField()),
                ('repository_url', models.URLField(max_length=2000)),
                ('description', models.TextField()),
                ('readme_url', models.URLField(max_length=2000)),
                ('readme', models.BinaryField()),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hub.category')),
            ],
            options={
                'db_table': 'exporters',
            },
        ),
        migrations.CreateModel(
            name='Official',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'officials',
            },
        ),
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('release_url', models.URLField(max_length=2000)),
                ('version', models.CharField(max_length=200)),
                ('commit_date', models.DateTimeField()),
                ('exporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hub.exporter')),
            ],
            options={
                'db_table': 'releases',
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('comment', models.TextField()),
                ('readme', models.BinaryField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('exporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hub.exporter')),
                ('official', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hub.official')),
            ],
            options={
                'db_table': 'logs',
            },
        ),
        migrations.AddField(
            model_name='exporter',
            name='official',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hub.official'),
        ),
    ]

# Generated by Django 4.2.6 on 2023-10-26 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('voters', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('currency', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('publisher', models.CharField(max_length=300)),
                ('page_count', models.IntegerField()),
                ('genres', models.CharField(max_length=200)),
            ],
        ),
    ]

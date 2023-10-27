# Generated by Django 4.2.4 on 2023-10-27 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        ('registerbook', '0003_book_seller'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='registerbook.book')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchased', to='main.profile')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sold', to='main.profile')),
            ],
        ),
    ]

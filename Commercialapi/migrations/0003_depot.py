# Generated by Django 4.1.5 on 2023-03-01 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Commercialapi', '0002_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='Depot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.IntegerField()),
                ('heure', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
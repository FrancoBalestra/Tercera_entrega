# Generated by Django 4.2.6 on 2023-11-03 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=30)),
                ('descripcion', models.TextField()),
                ('año', models.IntegerField()),
            ],
        ),
    ]

# Generated by Django 4.2.7 on 2023-11-24 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account1', '0002_rename_user_datosextra_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosextra',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatares'),
        ),
    ]

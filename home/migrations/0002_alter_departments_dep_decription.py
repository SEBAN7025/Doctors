# Generated by Django 4.2.4 on 2023-08-09 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departments',
            name='dep_decription',
            field=models.TextField(max_length=100),
        ),
    ]

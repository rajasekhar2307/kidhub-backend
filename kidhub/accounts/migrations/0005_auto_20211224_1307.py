# Generated by Django 3.0 on 2021-12-24 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20211223_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='admission_number',
            field=models.BigIntegerField(auto_created=True, unique=True),
        ),
    ]

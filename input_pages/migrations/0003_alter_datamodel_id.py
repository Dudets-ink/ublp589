# Generated by Django 4.0.6 on 2022-07-22 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('input_pages', '0002_alter_datamodel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datamodel',
            name='id',
            field=models.BigIntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 3.0.6 on 2020-10-12 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20201012_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='test',
            field=models.IntegerField(null=True),
        ),
    ]

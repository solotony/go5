# Generated by Django 3.0.6 on 2020-10-12 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20201012_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='test',
            field=models.CharField(max_length=20, null=True),
        ),
    ]

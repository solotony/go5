# Generated by Django 3.0.6 on 2020-07-07 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20200707_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='comment',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Address comment'),
        ),
    ]

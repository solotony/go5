# Generated by Django 3.0.6 on 2020-07-07 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20200707_1533'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cluster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Cluster title')),
                ('handle', models.SlugField(help_text='case insensitive', max_length=32, unique=True, verbose_name='Handle')),
            ],
            options={
                'verbose_name': 'Cluster',
                'verbose_name_plural': 'Clusters',
            },
        ),
        migrations.RemoveField(
            model_name='discountpolicy',
            name='group',
        ),
        migrations.RemoveField(
            model_name='product',
            name='group',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.AddField(
            model_name='discountpolicy',
            name='cluster',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='store.Cluster', verbose_name='Products cluster'),
        ),
        migrations.AddField(
            model_name='product',
            name='cluster',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='store.Cluster', verbose_name='Cluster'),
            preserve_default=False,
        ),
    ]

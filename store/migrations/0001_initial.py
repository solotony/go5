# Generated by Django 3.0.6 on 2020-07-04 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_seo_title', models.CharField(blank=True, max_length=200, null=True, verbose_name='SEO title')),
                ('_seo_description', models.CharField(blank=True, max_length=400, null=True, verbose_name='SEO description')),
                ('slug', models.CharField(blank=True, max_length=200, null=True, unique=True, verbose_name='slug')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creation time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Modification time')),
                ('name', models.CharField(max_length=200, verbose_name='Category title')),
                ('has_products', models.BooleanField(default=True, help_text='***help_text*** Has products', verbose_name='Has products')),
                ('show_products', models.BooleanField(default=True, help_text='***help_text*** Show products', verbose_name='Show products')),
                ('show_subcategory_products', models.BooleanField(default=True, help_text='***help_text*** Show subcategories products', verbose_name='Show subcategories products')),
                ('custom_characters', models.BooleanField(default=False, help_text='***help_text*** Custom characters', verbose_name='Custom characters')),
                ('default_digital', models.NullBooleanField(default=None, verbose_name='Default digital')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Price type title')),
                ('symbol', models.CharField(max_length=10, verbose_name='Price symbol')),
                ('symbol_before', models.BooleanField(default=False, verbose_name='Price symbol before value')),
                ('handle', models.SlugField(help_text='case insensitive', max_length=32, unique=True, verbose_name='Handle')),
            ],
            options={
                'verbose_name': 'Currency',
                'verbose_name_plural': 'Currencies',
            },
        ),
        migrations.CreateModel(
            name='PriceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Price type title')),
                ('handle', models.SlugField(help_text='case insensitive', max_length=32, unique=True, verbose_name='Handle')),
            ],
            options={
                'verbose_name': 'Price type',
                'verbose_name_plural': 'Prices types',
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Stock name')),
                ('handle', models.SlugField(help_text='case insensitive', max_length=32, unique=True, verbose_name='Handle')),
            ],
            options={
                'verbose_name': 'Stock',
                'verbose_name_plural': 'Stocks',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Supplier name')),
                ('handle', models.SlugField(help_text='case insensitive', max_length=32, unique=True, verbose_name='Handle')),
            ],
            options={
                'verbose_name': 'Supplier',
                'verbose_name_plural': 'Suppliers',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Unit title')),
                ('symbol', models.CharField(max_length=200, verbose_name='Unit symbol')),
                ('handle', models.SlugField(help_text='case insensitive', max_length=32, unique=True, verbose_name='Handle')),
                ('metric', models.BooleanField(choices=[(True, 'Metric'), (False, 'Us')], verbose_name='Measurement system')),
                ('type', models.CharField(choices=[('Item', 'Item'), ('Weight', 'Weight'), ('Length', 'Length'), ('Volume', 'Volume'), ('Voltage', 'Voltage'), ('Power', 'Power')], max_length=20, verbose_name='')),
            ],
            options={
                'verbose_name': 'Unit',
                'verbose_name_plural': 'Units',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_seo_title', models.CharField(blank=True, max_length=200, null=True, verbose_name='SEO title')),
                ('_seo_description', models.CharField(blank=True, max_length=400, null=True, verbose_name='SEO description')),
                ('slug', models.CharField(blank=True, max_length=200, null=True, unique=True, verbose_name='slug')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creation time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Modification time')),
                ('articul', models.CharField(max_length=100, unique=True, verbose_name='Аrticle')),
                ('name', models.CharField(max_length=200, verbose_name='Product name')),
                ('digital', models.BooleanField(default=False, verbose_name='Digital')),
                ('package_volume', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Package Volume')),
                ('package_weight', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Package Weight')),
                ('package_count', models.PositiveIntegerField(verbose_name='Package Count')),
                ('categories', models.ManyToManyField(blank=True, related_name='product', related_query_name='products', to='store.Category', verbose_name='Categories')),
                ('components', models.ManyToManyField(blank=True, related_name='complects', related_query_name='complect', to='store.Product', verbose_name='Product')),
                ('master', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='skus', related_query_name='sku', to='store.Product', verbose_name='Product')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', related_query_name='product', to='store.Unit', verbose_name='Unit')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Product',
            },
        ),
        migrations.CreateModel(
            name='ParentPivot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inheritance', models.BooleanField(default=True, help_text='***help_text*** Character inheritance', verbose_name='Character inheritance')),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent_refs', to='store.Category', verbose_name='Child category')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child_refs', to='store.Category', verbose_name='Parent category')),
            ],
            options={
                'verbose_name': 'Parent category',
                'verbose_name_plural': 'Parent categories',
            },
        ),
        migrations.CreateModel(
            name='MpttNode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tree_id', models.IntegerField(db_index=True)),
                ('inheriters_tree', models.BooleanField(db_index=True)),
                ('mptt_left', models.IntegerField(db_index=True)),
                ('mptt_right', models.IntegerField(db_index=True)),
                ('mptt_level', models.IntegerField(db_index=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internal_name', models.CharField(max_length=100, unique=True, verbose_name='Internal character name')),
                ('handle', models.SlugField(help_text='case insensitive', max_length=32, unique=True, verbose_name='Hadle')),
                ('public_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Public character name')),
                ('help_text', models.CharField(blank=True, max_length=250, null=True, verbose_name='Help text')),
                ('info', models.TextField(blank=True, null=True, verbose_name='Detailed description')),
                ('filterable', models.BooleanField(default=True)),
                ('position', models.PositiveSmallIntegerField(editable=False, verbose_name='Character position in search map')),
                ('character_type', models.IntegerField(choices=[(1, 'Integer value'), (2, 'Float value'), (5, 'Fixed decimal value'), (6, 'Set of string values')], default=1)),
                ('unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='store.Unit', verbose_name="Character's unit")),
            ],
            options={
                'verbose_name': 'Character',
                'verbose_name_plural': 'Characters',
            },
        ),
        migrations.CreateModel(
            name='CategoryCharacterPivot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Category')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Character')),
            ],
            options={
                'verbose_name': 'Category character',
                'verbose_name_plural': 'Category characters',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='characters',
            field=models.ManyToManyField(through='store.CategoryCharacterPivot', to='store.Character', verbose_name='Custom category characters'),
        ),
        migrations.AddField(
            model_name='category',
            name='default_stock',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categories', related_query_name='category', to='store.Stock', verbose_name='Default Supplier'),
        ),
        migrations.AddField(
            model_name='category',
            name='default_supplier',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categories', related_query_name='category', to='store.Supplier', verbose_name='Default Supplier'),
        ),
        migrations.AddField(
            model_name='category',
            name='parents',
            field=models.ManyToManyField(related_name='childs', related_query_name='child', through='store.ParentPivot', to='store.Category', verbose_name='Parent categories'),
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.BigIntegerField(verbose_name='Value')),
                ('computed', models.BooleanField(verbose_name='Complect computed price')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', related_query_name='price', to='store.Currency', verbose_name='Currency')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', related_query_name='price', to='store.Product', verbose_name='Product')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', related_query_name='price', to='store.PriceType', verbose_name='Price type')),
            ],
            options={
                'verbose_name': 'Price',
                'verbose_name_plural': 'Prices',
                'unique_together': {('type', 'product')},
            },
        ),
        migrations.CreateModel(
            name='CharacterValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=100, verbose_name='Character value')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='values', to='store.Character', verbose_name='Character')),
            ],
            options={
                'verbose_name': 'Character value',
                'verbose_name_plural': 'Character values',
                'unique_together': {('character', 'value')},
            },
        ),
    ]
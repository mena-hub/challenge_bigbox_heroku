# Generated by Django 2.2 on 2021-05-15 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='nombre')),
                ('internal_name', models.CharField(max_length=200, verbose_name='nombre interno')),
                ('description', models.TextField(verbose_name='descripción')),
                ('purchase_available', models.BooleanField(default=False, verbose_name='disponible venta individual')),
            ],
            options={
                'verbose_name': 'experiencia',
                'verbose_name_plural': 'experiencias',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='nombre')),
                ('slug', models.SlugField(verbose_name='slug')),
                ('order', models.IntegerField(default=0, verbose_name='orden')),
                ('description', models.TextField(verbose_name='descripción')),
            ],
            options={
                'verbose_name': 'categoría',
                'verbose_name_plural': 'categorías',
            },
        ),
        migrations.CreateModel(
            name='Reason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='nombre')),
                ('slug', models.SlugField(verbose_name='slug')),
                ('order', models.IntegerField(default=0, verbose_name='orden')),
            ],
            options={
                'verbose_name': 'ocasión',
                'verbose_name_plural': 'ocasiones',
            },
        ),
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='nombre')),
                ('internal_name', models.CharField(max_length=200, verbose_name='nombre interno')),
                ('description', models.TextField(verbose_name='descripción')),
                ('price', models.IntegerField(verbose_name='precio de venta')),
                ('purchase_available', models.BooleanField(default=False, verbose_name='disponible venta individual')),
                ('slug', models.CharField(blank=True, max_length=200, null=True, verbose_name='slug')),
                ('activities', models.ManyToManyField(to='bigbox.Activity', verbose_name='experiencias')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bigbox.Category', verbose_name='categorías')),
            ],
            options={
                'verbose_name': 'box',
                'verbose_name_plural': 'boxes',
            },
        ),
        migrations.AddField(
            model_name='activity',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bigbox.Category', verbose_name='categorías'),
        ),
        migrations.AddField(
            model_name='activity',
            name='reasons',
            field=models.ManyToManyField(blank=True, to='bigbox.Reason', verbose_name='ocasiones'),
        ),
    ]

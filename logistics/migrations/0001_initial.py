# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-12-14 15:53
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True, verbose_name='Name')),
                ('state', models.CharField(choices=[('Montevideo', 'Montevideo'), ('Artigas', 'Artigas'), ('Canelones', 'Canelones'), ('Cerro Largo', 'Cerro Largo'), ('Colonia', 'Colonia'), ('Durazno', 'Durazno'), ('Flores', 'Flores'), ('Florida', 'Florida'), ('Lavalleja', 'Lavalleja'), ('Maldonado', 'Maldonado'), ('Paysand\xfa', 'Paysand\xfa'), ('R\xedo Negro', 'R\xedo Negro'), ('Rivera', 'Rivera'), ('Rocha', 'Rocha'), ('Salto', 'Salto'), ('San Jos\xe9', 'San Jos\xe9'), ('Soriano', 'Soriano'), ('Tacuaremb\xf3', 'Tacuaremb\xf3'), ('Treinta y Tres', 'Treinta y Tres')], max_length=20, verbose_name='City')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'city',
                'verbose_name_plural': 'cities',
            },
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date')),
                ('route', models.IntegerField(verbose_name='Route')),
                ('copies', models.IntegerField(verbose_name='Copies')),
            ],
            options={
                'verbose_name': 'delivery',
                'verbose_name_plural': 'deliveries',
            },
        ),
        migrations.CreateModel(
            name='Edition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date')),
                ('start_time', models.TimeField(blank=True, null=True, verbose_name='Start time')),
                ('end_time', models.TimeField(blank=True, null=True, verbose_name='End Time')),
                ('standard', models.IntegerField(blank=True, null=True, verbose_name='Standard')),
                ('digital', models.IntegerField(blank=True, null=True, verbose_name='Digital')),
                ('free', models.IntegerField(blank=True, null=True, verbose_name='Free')),
                ('promotions', models.IntegerField(blank=True, null=True, verbose_name='Promotions')),
                ('total', models.IntegerField(blank=True, null=True, verbose_name='Total')),
                ('rounding', models.IntegerField(blank=True, null=True)),
                ('old_pk', models.PositiveIntegerField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'edition',
                'verbose_name_plural': 'editions',
            },
        ),
        migrations.CreateModel(
            name='EditionProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('additional_copies', models.PositiveSmallIntegerField(default=3, verbose_name='Additional copies')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Product', verbose_name='Product')),
            ],
        ),
        migrations.CreateModel(
            name='EditionRoute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promotions', models.IntegerField(blank=True, null=True, verbose_name='Promotions')),
                ('edition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logistics.Edition', verbose_name='Edition')),
            ],
            options={
                'verbose_name': 'edition route',
                'verbose_name_plural': 'edition routes',
            },
        ),
        migrations.CreateModel(
            name='GeorefAddress',
            fields=[
                ('gid', models.IntegerField(primary_key=True, serialize=False, verbose_name='gid')),
                ('street_name', models.CharField(max_length=36, verbose_name='Street name')),
                ('street_number', models.IntegerField(verbose_name='Street number')),
                ('letter', models.CharField(blank=True, max_length=5, null=True, verbose_name='Letter')),
                ('the_geom', django.contrib.gis.db.models.fields.PointField(srid=32721)),
            ],
            options={
                'ordering': ('street_number',),
                'verbose_name': 'geo ref address',
                'verbose_name_plural': 'geo ref addresses',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(choices=[(b'P', 'Prints'), (b'L', 'Labels')], max_length=20, unique=True, verbose_name='Place')),
                ('text', models.TextField(blank=True, verbose_name='Text')),
            ],
            options={
                'verbose_name': 'message',
                'verbose_name_plural': 'messages',
            },
        ),
        migrations.CreateModel(
            name='PickupPlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'ordering': ('resort',),
                'verbose_name': 'pickup place',
                'verbose_name_plural': 'pickup places',
            },
        ),
        migrations.CreateModel(
            name='PickupPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Name')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Address')),
                ('old_pk', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'pickup point',
                'verbose_name_plural': 'pickup points',
            },
        ),
        migrations.CreateModel(
            name='Resort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('Montevideo', 'Montevideo'), ('Artigas', 'Artigas'), ('Canelones', 'Canelones'), ('Cerro Largo', 'Cerro Largo'), ('Colonia', 'Colonia'), ('Durazno', 'Durazno'), ('Flores', 'Flores'), ('Florida', 'Florida'), ('Lavalleja', 'Lavalleja'), ('Maldonado', 'Maldonado'), ('Paysand\xfa', 'Paysand\xfa'), ('R\xedo Negro', 'R\xedo Negro'), ('Rivera', 'Rivera'), ('Rocha', 'Rocha'), ('Salto', 'Salto'), ('San Jos\xe9', 'San Jos\xe9'), ('Soriano', 'Soriano'), ('Tacuaremb\xf3', 'Tacuaremb\xf3'), ('Treinta y Tres', 'Treinta y Tres')], max_length=20, verbose_name='State')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('status', models.CharField(choices=[(b'AC', 'To be confirmed'), (b'NL', "We don't deliver there"), (b'P', 'Door to door'), (b'R', 'Withdrawal')], max_length=2, verbose_name='Status')),
                ('confirmation_date', models.DateField(blank=True, null=True, verbose_name='Confirmation date')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Notes')),
                ('arrival_time', models.TimeField(blank=True, null=True, verbose_name='Arrival time')),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name='Order')),
            ],
            options={
                'ordering': ('order',),
                'verbose_name': 'resort',
                'verbose_name_plural': 'resorts',
            },
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('number', models.IntegerField(primary_key=True, serialize=False, verbose_name='Number')),
                ('name', models.CharField(max_length=40, verbose_name='Name')),
                ('state', models.CharField(max_length=20, verbose_name='State')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('distributor', models.CharField(blank=True, max_length=40, verbose_name='Distributor')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='Phone')),
                ('mobile', models.CharField(blank=True, max_length=20, verbose_name='Mobile')),
                ('email', models.CharField(blank=True, max_length=100, verbose_name='Email')),
                ('delivery_place', models.CharField(blank=True, max_length=40, verbose_name='Delivery place')),
                ('arrival_time', models.TimeField(blank=True, null=True, verbose_name='Arrival time')),
                ('additional_copies', models.PositiveSmallIntegerField(default=3, verbose_name='Additional copies')),
                ('directions', models.TextField(blank=True, verbose_name='Directions')),
                ('distributor_directions', models.TextField(blank=True, null=True, verbose_name='Distributor directions')),
                ('notes', models.TextField(blank=True, verbose_name='Notes')),
                ('beach', models.BooleanField(default=False, verbose_name='Beach')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('price_per_copy', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Price per copy')),
                ('parent_route', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_route', to='logistics.Route', verbose_name='Parent route')),
            ],
            options={
                'ordering': ('number',),
                'verbose_name': 'Route',
                'verbose_name_plural': 'Routes',
            },
        ),
        migrations.CreateModel(
            name='RouteChange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateTimeField(auto_now_add=True, verbose_name='Dt')),
                ('old_address', models.CharField(max_length=255, null=True, verbose_name='Old address')),
                ('old_city', models.CharField(max_length=20, null=True, verbose_name='Old city')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Contact', verbose_name='Contact')),
                ('old_route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logistics.Route', verbose_name='Old route')),
            ],
            options={
                'verbose_name': 'route change',
                'verbose_name_plural': 'route changes',
            },
        ),
        migrations.AddField(
            model_name='resort',
            name='route',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='logistics.Route', verbose_name='Route'),
        ),
        migrations.AddField(
            model_name='pickupplace',
            name='resort',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logistics.Resort', verbose_name='Resort'),
        ),
        migrations.AddField(
            model_name='editionroute',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logistics.Route', verbose_name='Route'),
        ),
        migrations.AddField(
            model_name='editionproduct',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logistics.Route', verbose_name='Route'),
        ),
        migrations.AlterUniqueTogether(
            name='edition',
            unique_together=set([('product', 'date')]),
        ),
    ]

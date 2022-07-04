# Generated by Django 4.0.5 on 2022-07-04 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=15)),
                ('car_name', models.CharField(max_length=50)),
                ('trim', models.CharField(max_length=50)),
                ('body_shape', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('model_year', models.CharField(max_length=50)),
                ('first_registration_year', models.CharField(max_length=50)),
                ('engine', models.CharField(max_length=50)),
                ('transmission', models.CharField(max_length=50)),
                ('manufacturer', models.CharField(max_length=50)),
                ('factory_price', models.BigIntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'db_table': 'cars',
            },
        ),
        migrations.CreateModel(
            name='Estimate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('mileage', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=30)),
                ('sunroof', models.BooleanField()),
                ('navigation', models.BooleanField()),
                ('ventilation_seat', models.BooleanField()),
                ('heated_seat', models.BooleanField()),
                ('electric_seat', models.BooleanField()),
                ('smart_key', models.BooleanField()),
                ('leather_seat', models.BooleanField()),
                ('electric_folding_mirrort', models.BooleanField()),
                ('accident_status', models.BooleanField()),
                ('spare_key', models.IntegerField()),
                ('wheel_scratch', models.IntegerField()),
                ('outer_plate_scratch', models.IntegerField()),
                ('other_maintenance_repair', models.TextField()),
                ('other_special', models.TextField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.car')),
            ],
            options={
                'db_table': 'estimates',
            },
        ),
        migrations.CreateModel(
            name='TransactionHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hsitory', models.CharField(max_length=50)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.car')),
            ],
            options={
                'db_table': 'transaction_histories',
            },
        ),
        migrations.CreateModel(
            name='InsuranceHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hsitory', models.CharField(max_length=50)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.car')),
            ],
            options={
                'db_table': 'insurance_histories',
            },
        ),
        migrations.CreateModel(
            name='EstimateCarImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_info', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=200)),
                ('estimate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.estimate')),
            ],
            options={
                'db_table': 'estimate_car_images',
            },
        ),
    ]

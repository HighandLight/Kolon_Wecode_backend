# Generated by Django 4.0.5 on 2022-07-04 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=15)),
                ('owner', models.CharField(max_length=100)),
                ('manufacturer', models.CharField(max_length=50)),
                ('car_name', models.CharField(max_length=50)),
                ('trim', models.CharField(max_length=50)),
                ('body_shape', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('model_year', models.CharField(max_length=50)),
                ('first_registration_year', models.CharField(max_length=50)),
                ('mileage', models.CharField(max_length=50)),
                ('engine', models.CharField(max_length=50)),
                ('transmission', models.CharField(max_length=50)),
                ('factory_price', models.BigIntegerField()),
                ('transaction_price', models.BigIntegerField()),
            ],
            options={
                'db_table': 'test_cars',
            },
        ),
        migrations.CreateModel(
            name='TestTransactionHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('history', models.CharField(max_length=50)),
                ('test_car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testcar.testcar')),
            ],
            options={
                'db_table': 'test_transaction_histories',
            },
        ),
        migrations.CreateModel(
            name='TestInsuranceHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('history', models.CharField(max_length=50)),
                ('test_car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testcar.testcar')),
            ],
            options={
                'db_table': 'test_insurance_histories',
            },
        ),
    ]

# Generated by Django 4.1.7 on 2023-04-04 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_user_deleted_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='RentItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_model', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=100)),
                ('person_name', models.CharField(max_length=100)),
                ('model_name', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=50)),
                ('number_plate', models.CharField(max_length=50, unique=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('rent_status', models.CharField(default=None, max_length=50)),
                ('mileage_limit', models.CharField(default=None, max_length=50)),
                ('additional_driver', models.CharField(blank=True, max_length=50)),
                ('user_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='api.user')),
            ],
        ),
    ]
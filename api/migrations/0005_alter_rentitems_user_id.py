# Generated by Django 4.1.7 on 2023-04-04 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rentitems'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentitems',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user'),
        ),
    ]

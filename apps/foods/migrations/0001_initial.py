# Generated by Django 3.2.7 on 2021-09-27 01:17

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurants', '0002_alter_restaurants_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name', max_length=255, verbose_name='Name')),
                ('description', models.CharField(help_text='Description', max_length=255, verbose_name='Description')),
                ('calories', models.FloatField(default=0.0, help_text='Calories', validators=[django.core.validators.MaxValueValidator(9999999)], verbose_name='Calories')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foods', to='restaurants.restaurants')),
            ],
        ),
    ]

# Generated by Django 3.2.2 on 2021-05-23 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacyapp', '0003_auto_20210523_2152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('employees', models.ManyToManyField(blank=True, to='pharmacyapp.Employee')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]
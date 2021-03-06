# Generated by Django 3.2.2 on 2021-05-13 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('address', models.TextField()),
                ('phone_no', models.DecimalField(decimal_places=0, max_digits=11)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('phone_no', models.DecimalField(decimal_places=0, max_digits=11)),
                ('email', models.EmailField(max_length=254)),
                ('id_proof', models.CharField(choices=[('a', 'Aadhar'), ('b', 'Driving License'), ('c', 'Ration Card'), ('d', 'PAN Card'), ('e', 'Passport')], default='a', help_text='Enter Vote', max_length=1)),
                ('proof_unique_no', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.DecimalField(decimal_places=0, max_digits=5)),
                ('name', models.CharField(max_length=200)),
                ('stock', models.DecimalField(decimal_places=0, max_digits=6)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(max_length=300)),
                ('address', models.TextField()),
                ('owner_name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('dealer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacyapp.dealer')),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacyapp.medicine')),
            ],
        ),
    ]

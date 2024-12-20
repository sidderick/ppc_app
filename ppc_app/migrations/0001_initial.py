# Generated by Django 4.2.11 on 2024-03-06 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonDetails',
            fields=[
                ('userID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('dateOfBirth', models.DateField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='CertificateDetails',
            fields=[
                ('certNumber', models.AutoField(primary_key=True, serialize=False)),
                ('exempt', models.BooleanField(default=False)),
                ('datePurchased', models.DateField()),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ppc_app.persondetails')),
            ],
        ),
    ]

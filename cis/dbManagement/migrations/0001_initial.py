# Generated by Django 4.2.2 on 2023-08-02 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facultyId', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('phoneNumber', models.CharField(max_length=12)),
                ('emailId', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=3)),
            ],
            options={
                'verbose_name_plural': 'Faculties',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phoneNumber', models.CharField(max_length=12)),
                ('displayPhNo', models.BooleanField()),
                ('emailId', models.CharField(max_length=50)),
                ('yearOfAddmission', models.IntegerField()),
                ('yearOfPassOut', models.IntegerField()),
                ('department', models.CharField(max_length=3)),
                ('remarks', models.CharField(max_length=100)),
            ],
        ),
    ]
# Generated by Django 5.0.1 on 2024-10-11 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_contact_user_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deparment', models.CharField(max_length=20)),
                ('doctor', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.CharField(max_length=20)),
                ('time', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='appointment',
        ),
    ]

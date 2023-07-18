# Generated by Django 4.2.3 on 2023-07-18 08:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender_status', models.CharField(choices=[('Female', 'female'), ('Male', 'male')], max_length=255)),
                ('id_number', models.CharField(max_length=255, unique=True)),
                ('phone_number', models.CharField(max_length=255, unique=True)),
                ('kra_pin', models.CharField(max_length=255, unique=True)),
                ('birth_date', models.DateField()),
                ('marital_status', models.CharField(choices=[('Married', 'married'), ('Divorced', 'divorced'), ('Single', 'single'), ('widowed', 'Widowed')], max_length=255)),
                ('town', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MpesaDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(max_length=200)),
                ('mpesa_number', models.CharField(max_length=200)),
                ('preferred_payment_day', models.CharField(max_length=200)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='FamilyMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('relationship', models.CharField(max_length=200)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('Female', 'female'), ('Male', 'male')], max_length=255)),
                ('marital_status', models.CharField(choices=[('Married', 'married'), ('Divorced', 'divorced'), ('Single', 'single'), ('widowed', 'Widowed')], max_length=255)),
                ('postal_code', models.CharField(max_length=255)),
                ('town', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('renew_date', models.DateField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Employment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employment_status', models.CharField(max_length=255)),
                ('employment_sector', models.CharField(blank=True, max_length=255, null=True)),
                ('salary', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('employer', models.CharField(blank=True, max_length=255, null=True)),
                ('position', models.CharField(blank=True, max_length=255, null=True)),
                ('date_employed', models.DateField(blank=True, null=True)),
                ('previous_employer', models.CharField(blank=True, max_length=255, null=True)),
                ('previous_salary', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('highest_education_level', models.CharField(max_length=255)),
                ('last_school_attended', models.CharField(max_length=255)),
                ('year_joined', models.CharField(blank=True, max_length=255, null=True)),
                ('graduation_year', models.CharField(blank=True, max_length=255, null=True)),
                ('course', models.CharField(blank=True, max_length=255, null=True)),
                ('grade', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.userprofile')),
            ],
        ),
    ]

# Generated by Django 4.0.3 on 2022-05-31 09:45

from django.conf import settings
import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=225, unique=True, verbose_name='email')),
                ('first_name', models.CharField(blank=True, max_length=225, null=True, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=225, null=True, verbose_name='last name')),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('age', models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(200), django.core.validators.MinValueValidator(0)])),
                ('sex', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('contact_number', models.CharField(blank=True, max_length=13, null=True, validators=[django.core.validators.RegexValidator('^(09|\\+639)\\d{9}$', message='Phone number must begin with +639 or 09 followed by a 9 digits')])),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('role', models.CharField(choices=[('SA', 'System Admin'), ('PT', 'Physical Therapist'), ('P', 'Patient')], max_length=2, verbose_name='role')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AccountRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=225)),
                ('role', models.CharField(blank=True, choices=[('SA', 'System Admin'), ('PT', 'Physical Therapist'), ('P', 'Patient')], max_length=2, verbose_name='role')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('denied', 'Denied')], default='pending', max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='PhysicalTherapistProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=225, null=True)),
                ('account', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Teleconsultation_Hours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teleconsultation_weekday', models.CharField(choices=[('MON', 'Monday'), ('TUE', 'Tuesday'), ('WED', 'Wednesday'), ('THU', 'Thursday'), ('FRI', 'Friday'), ('SAT', 'Saturday'), ('SUN', 'Sunday')], default='MON', max_length=9)),
                ('teleconsultation_hours', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.TimeField(verbose_name='teleconsultation_time'), size=None), size=None)),
                ('pt', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='webapp.physicaltherapistprofile')),
            ],
        ),
        migrations.CreateModel(
            name='SystemAdminProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=225, null=True)),
                ('account', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PatientProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=225, null=True)),
                ('account', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(default='Subject', max_length=256)),
                ('text', models.CharField(default='Hello', max_length=256)),
                ('date_sent', models.DateTimeField(auto_now_add=True, verbose_name='date sent')),
                ('receiver', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Clinic_Hours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekday', models.CharField(choices=[('MON', 'Monday'), ('TUES', 'Tuesday'), ('WED', 'Wednesday'), ('THURS', 'Thursday'), ('FRI', 'Friday'), ('SAT', 'Saturday'), ('SUN', 'Sunday')], default='MON', max_length=5, verbose_name='weekday')),
                ('hours', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.TimeField(verbose_name='hours'), size=None), size=None)),
                ('pt', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='webapp.physicaltherapistprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('teleconsultation', 'teleconsultation'), ('clinical', 'Clinical')], default='teleconsultation', max_length=16)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('reschedule', 'Reschedule'), ('cancelled', 'Cancelled'), ('finished', 'Finished')], default='pending', max_length=10)),
                ('title', models.TextField(default='text title')),
                ('description', models.TextField(default='text description')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('patient', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='webapp.patientprofile')),
                ('pt', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='webapp.physicaltherapistprofile')),
            ],
        ),
    ]

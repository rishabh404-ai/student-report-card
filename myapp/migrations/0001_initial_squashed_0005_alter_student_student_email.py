# Generated by Django 3.2.5 on 2021-08-14 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('myapp', '0001_initial'), ('myapp', '0002_alter_student_passing_status'), ('myapp', '0003_celerytaskjobstatus'), ('myapp', '0004_alter_student_student_email'), ('myapp', '0005_alter_student_student_email')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=200)),
                ('student_roll_no', models.IntegerField(unique=True)),
                ('student_class', models.CharField(max_length=200)),
                ('passing_status', models.CharField(blank=True, choices=[('Pass', 'Pass'), ('Fail', 'Fail')], default=None, max_length=4, null=True)),
                ('student_school_name', models.CharField(max_length=200)),
                ('date_of_report', models.DateField(auto_now_add=True)),
                ('student_email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_subject', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('students_marks', models.FloatField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.student')),
                ('student_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.subject')),
            ],
        ),
        migrations.CreateModel(
            name='CeleryTaskJobStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_id', models.CharField(max_length=1000)),
                ('job_status', models.CharField(max_length=100)),
            ],
        ),
    ]

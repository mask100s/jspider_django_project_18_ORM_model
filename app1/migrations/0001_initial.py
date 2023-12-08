# Generated by Django 4.2.7 on 2023-12-08 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bonus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('deptno', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('dname', models.CharField(max_length=14)),
                ('loc', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='Salgrade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.PositiveIntegerField()),
                ('losal', models.PositiveIntegerField()),
                ('hisal', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('empno', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=10)),
                ('job', models.CharField(max_length=9)),
                ('mgr', models.PositiveIntegerField()),
                ('hiredate', models.DateField()),
                ('sal', models.PositiveIntegerField()),
                ('comm', models.PositiveIntegerField()),
                ('deptno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.dept')),
            ],
        ),
    ]

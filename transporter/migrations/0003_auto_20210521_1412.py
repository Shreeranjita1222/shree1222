# Generated by Django 3.2.3 on 2021-05-21 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transporter', '0002_auto_20210521_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routes',
            name='cost',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='routes',
            name='destination',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='routes',
            name='origin',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='schedules',
            name='field_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='schedules',
            name='route',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='passengerid',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='schedulesid',
            field=models.IntegerField(),
        ),
    ]

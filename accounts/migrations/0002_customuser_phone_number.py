# Generated by Django 4.0 on 2024-01-24 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(default=8801755215173, max_length=30, verbose_name='Phone Number'),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.2.15 on 2022-11-07 06:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20221106_0948'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribedusers',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date created'),
        ),
        migrations.AlterField(
            model_name='subscribedusers',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='subscribedusers',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]

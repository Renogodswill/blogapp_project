# Generated by Django 3.2.15 on 2022-10-04 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='feature_image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]

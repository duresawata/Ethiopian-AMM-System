# Generated by Django 3.2 on 2022-02-06 14:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_myproducts_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='myproducts',
            name='img',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='pics'),
            preserve_default=False,
        ),
    ]

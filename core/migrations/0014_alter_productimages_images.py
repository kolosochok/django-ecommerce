# Generated by Django 4.2.1 on 2023-11-08 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_vendor_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimages',
            name='images',
            field=models.ImageField(default='p_image1.jpg', upload_to='product-images'),
        ),
    ]
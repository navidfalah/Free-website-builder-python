# Generated by Django 4.0.2 on 2022-03-14 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_myshop_province'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sale_availble',
            field=models.BooleanField(default=True, verbose_name='کالا قابل فروش در سایت است؟'),
        ),
    ]
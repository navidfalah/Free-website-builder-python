# Generated by Django 4.0.2 on 2022-03-28 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_blogmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
# Generated by Django 3.1.1 on 2020-09-14 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200914_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pid',
            field=models.CharField(max_length=254, primary_key=True, serialize=False),
        ),
    ]

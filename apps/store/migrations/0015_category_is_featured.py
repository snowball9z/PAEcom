# Generated by Django 3.1 on 2021-04-07 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_category_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]
# Generated by Django 4.0.3 on 2022-03-18 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_news_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='body',
            field=models.TextField(),
        ),
    ]
# Generated by Django 2.1.7 on 2019-02-22 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_article_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='source',
            field=models.CharField(default='The Guardian', max_length=120),
            preserve_default=False,
        ),
    ]

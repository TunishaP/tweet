# Generated by Django 4.1.1 on 2022-09-22 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='likes',
            field=models.PositiveBigIntegerField(blank=True, db_index=True, default=0, verbose_name='like'),
        ),
    ]

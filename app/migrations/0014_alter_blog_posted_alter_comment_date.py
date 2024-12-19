# Generated by Django 4.2.16 on 2024-12-18 12:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_product_alter_blog_posted_alter_comment_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2024, 12, 18, 15, 39, 22, 600973), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2024, 12, 18, 15, 39, 22, 601970), verbose_name='Дата комментария'),
        ),
    ]

# Generated by Django 5.0.6 on 2024-05-26 08:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='blog.blog'),
        ),
        migrations.AlterField(
            model_name='like',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like', to='blog.blog'),
        ),
        migrations.AlterField(
            model_name='postviews',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='view_count', to='blog.blog'),
        ),
    ]

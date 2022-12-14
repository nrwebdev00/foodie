# Generated by Django 4.1 on 2022-09-02 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_recipe_featured_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='alt_image',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='recipe_images',
            name='alt',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='recipe_video',
            name='alt',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

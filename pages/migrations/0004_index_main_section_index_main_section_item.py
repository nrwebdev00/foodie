# Generated by Django 4.1 on 2022-08-30 19:12

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('pages', '0003_featured_recipe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Index_Main_Section',
            fields=[
                ('title', models.CharField(default='Main Section Title', max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Index_Main_Section_Item',
            fields=[
                ('url_name', models.CharField(default='home-page', max_length=200)),
                ('img', models.ImageField(upload_to='index_main_section/')),
                ('alt', models.CharField(default='Main Section Image', max_length=200)),
                ('title', models.CharField(default='Main Section Title', max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('index_main_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.index_main_section')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.profile')),
            ],
        ),
    ]

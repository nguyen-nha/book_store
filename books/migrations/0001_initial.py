# Generated by Django 4.1 on 2022-08-17 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=255)),
                ('writer', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('published_date', models.DateTimeField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_of_comment', models.CharField(max_length=255)),
                ('comment', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='books.book')),
            ],
        ),
    ]

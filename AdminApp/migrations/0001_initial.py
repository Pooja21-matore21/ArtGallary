# Generated by Django 4.1.6 on 2023-02-22 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Mehandi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mehandi_name', models.CharField(max_length=20)),
                ('price', models.FloatField(default=200)),
                ('description', models.CharField(max_length=200)),
                ('image', models.ImageField(default='pic', upload_to='Images')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.category')),
            ],
            options={
                'db_table': 'Mehandi',
            },
        ),
    ]
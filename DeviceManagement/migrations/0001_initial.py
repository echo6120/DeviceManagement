# Generated by Django 2.0 on 2020-01-26 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleColumn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('System', models.CharField(max_length=200)),
                ('created', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
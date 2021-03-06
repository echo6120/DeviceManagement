# Generated by Django 2.0 on 2020-01-28 08:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('DeviceManagement', '0002_auto_20200126_1715'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_name', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('owner', models.CharField(max_length=200)),
                ('borrow', models.CharField(max_length=200)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('device_system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='device', to='DeviceManagement.DeviceSystem')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.AlterIndexTogether(
            name='device',
            index_together={('id', 'device_name')},
        ),
    ]

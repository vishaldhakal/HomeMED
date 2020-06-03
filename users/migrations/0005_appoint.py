# Generated by Django 3.0.6 on 2020-06-02 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200602_1213'),
    ]

    operations = [
        migrations.CreateModel(
            name='appoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doct', to='users.userProfile')),
                ('pate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pate', to='users.userProfile')),
            ],
        ),
    ]

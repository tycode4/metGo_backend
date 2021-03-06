# Generated by Django 3.2.5 on 2021-07-28 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('masters', '0002_initial'),
        ('services', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('content', models.TextField(max_length=2000, null=True)),
                ('rating', models.PositiveIntegerField()),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='masters.master')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_reviews', to='services.service')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'db_table': 'reviews',
            },
        ),
    ]

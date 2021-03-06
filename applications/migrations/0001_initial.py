# Generated by Django 3.2.5 on 2021-07-28 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('age', models.PositiveIntegerField(choices=[(10, 'Ten'), (20, 'Twenty'), (30, 'Thirty'), (40, 'Fourty'), (50, 'Fifity')], null=True)),
                ('career', models.PositiveIntegerField(choices=[(0, 'Zero'), (5, 'Five Years'), (10, 'Ten Years'), (15, 'Over Fifteen Years')], null=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=20, null=True)),
            ],
            options={
                'db_table': 'applications',
            },
        ),
    ]

# Generated by Django 4.1.1 on 2022-09-22 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=20)),
                ('order_date', models.DateField()),
                ('quantity', models.CharField(max_length=5)),
            ],
        ),
    ]

# Generated by Django 5.0.3 on 2024-04-17 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groceries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('date_of_creation', models.DateTimeField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.DeleteModel(
            name='grocery_list',
        ),
        migrations.AlterModelOptions(
            name='grocery',
            options={'ordering': ['name']},
        ),
        migrations.RemoveField(
            model_name='grocery',
            name='price',
        ),
        migrations.AlterField(
            model_name='grocery',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AddField(
            model_name='glist',
            name='groceries',
            field=models.ManyToManyField(to='groceries.grocery'),
        ),
    ]

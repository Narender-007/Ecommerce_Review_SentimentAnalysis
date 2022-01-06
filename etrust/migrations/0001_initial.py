# Generated by Django 3.0.4 on 2020-03-10 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=300)),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('user', models.CharField(max_length=60)),
                ('product', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.CharField(max_length=30)),
                ('manufacturer', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=300)),
                ('path', models.FileField(upload_to='products')),
            ],
        ),
        migrations.CreateModel(
            name='RatingModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(default='0', max_length=100)),
                ('user', models.CharField(max_length=60)),
                ('product', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SearchHistoryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.TextField(max_length=300)),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('user', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=100)),
                ('productid', models.CharField(max_length=100)),
                ('tdate', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
    ]

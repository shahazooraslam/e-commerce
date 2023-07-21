# Generated by Django 4.1.7 on 2023-07-03 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=14)),
                ('confirmpassword', models.CharField(max_length=14)),
                ('name', models.CharField(max_length=14)),
            ],
        ),
        migrations.CreateModel(
            name='gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('description', models.TextField(max_length=255)),
                ('sellingprice', models.CharField(max_length=100)),
                ('discountprice', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.EmailField(max_length=254)),
                ('product_name', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('price', models.IntegerField(default=0)),
                ('ordered_date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('ACCEPTED', 'ACCEPTED'), ('PACKED', 'PACKED'), ('ON THE WAY', 'ON THEWAY'), ('DELIVERED', 'DELIVERD'), ('CANCELED', 'CANCELED')], default='pending', max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('price', models.IntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authen.gallery')),
            ],
        ),
    ]

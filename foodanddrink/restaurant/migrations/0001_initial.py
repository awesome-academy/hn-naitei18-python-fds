# Generated by Django 3.1 on 2020-08-21 08:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter category name', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(null=True, upload_to='media/profile_pics')),
                ('address', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(default=django.utils.timezone.now)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('code', models.CharField(max_length=200)),
                ('status', models.CharField(blank=True, choices=[('p', 'PENDING'), ('f', 'FINISH'), ('c', 'CANCEL')], default='p', max_length=1)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.customer')),
            ],
            options={
                'ordering': ['-date_ordered'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(default=None, null=True, upload_to='media/product_pics')),
                ('description', models.TextField(help_text='Enter description of product', max_length=1000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('quantity', models.IntegerField()),
                ('vote', models.FloatField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.category')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(help_text='Enter description of review', max_length=1000)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.customer')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('amount', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.product')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(help_text='Enter content of comment', max_length=1000)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.review')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.customer')),
            ],
        ),
    ]

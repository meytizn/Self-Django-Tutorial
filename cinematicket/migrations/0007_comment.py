# Generated by Django 4.0.6 on 2024-08-21 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinematicket', '0006_alter_food_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='نام کاربری ')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل ')),
                ('message', models.TextField(verbose_name='متن نظر')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='انتشار')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='food', to='cinematicket.food', verbose_name='غذا')),
            ],
        ),
    ]

# Generated by Django 2.0.1 on 2019-08-28 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0016_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='FruitCartEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnt', models.IntegerField(default=1, verbose_name='数量')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Cart', verbose_name='购物车编号')),
                ('fruit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.FruitEntity', verbose_name='水果名')),
            ],
            options={
                'verbose_name': '购物车详情',
                'verbose_name_plural': '购物车详情',
                'db_table': 't_fruit_cart',
            },
        ),
    ]

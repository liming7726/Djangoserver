# Generated by Django 2.0.1 on 2019-08-31 02:08

from django.db import migrations, models
import django.db.models.manager
import mainapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0019_auto_20190829_1048'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='userentity',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='userentity',
            name='pwd',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='密码'),
        ),
        migrations.AlterField(
            model_name='fruitentity',
            name='tags',
            field=models.ManyToManyField(blank=True, db_table='t_fruit_tags', null=True, related_name='fruits', to='mainapp.TagEntity', verbose_name='标签名'),
        ),
        migrations.AlterField(
            model_name='fruitentity',
            name='users',
            field=models.ManyToManyField(blank=True, db_table='t_collect', null=True, related_name='fruits', to='mainapp.UserEntity', verbose_name='收藏列表'),
        ),
        migrations.AlterField(
            model_name='userentity',
            name='phone',
            field=models.CharField(blank=True, max_length=11, null=True, validators=[mainapp.models.UserValidator.valid_phone], verbose_name='手机号'),
        ),
    ]

# Generated by Django 2.0.1 on 2019-08-28 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0013_auto_20190828_1457'),
    ]

    operations = [
        migrations.CreateModel(
            name='RealProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rel_name', models.CharField(max_length=20, verbose_name='真实姓名')),
                ('number', models.CharField(max_length=30, verbose_name='证件号')),
                ('real_type', models.IntegerField(choices=[(0, '身份证'), (1, '护照'), (2, '驾驶证')], verbose_name='证件类型')),
                ('image1', models.ImageField(upload_to='user/real', verbose_name='正面照')),
                ('image2', models.ImageField(upload_to='user/real', verbose_name='反面照')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainapp.UserEntity', verbose_name='账号')),
            ],
            options={
                'verbose_name': '实名认证表',
                'verbose_name_plural': '实名认证表',
                'db_table': 't_user_profile',
            },
        ),
    ]

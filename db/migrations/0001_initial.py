# Generated by Django 2.0 on 2018-03-29 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('asset', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='db_mysql',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=64, unique=True, verbose_name='数据库名字')),
                ('ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='IP')),
                ('port', models.IntegerField(blank=True, default='3306', null=True, verbose_name='端口')),
                ('model', models.CharField(blank=True, max_length=128, null=True, verbose_name='数据库型号')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否启用')),
                ('ps', models.CharField(blank=True, max_length=1024, null=True, verbose_name='备注')),
                ('ctime', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('utime', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('data_center', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='asset.data_centers', verbose_name='数据中心')),
            ],
            options={
                'verbose_name': '数据库管理',
                'verbose_name_plural': '数据库管理',
                'db_table': 'db_mysql',
                'permissions': {('task_db_mysql', '执行数据库资产'), ('read_db_mysql', '只读数据库资产')},
            },
        ),
        migrations.CreateModel(
            name='db_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='名称')),
                ('username', models.CharField(blank=True, default='root', max_length=64, null=True, verbose_name='登陆用户')),
                ('password', models.CharField(blank=True, max_length=255, null=True, verbose_name='登陆密码')),
                ('ps', models.CharField(blank=True, max_length=1024, null=True, verbose_name='备注')),
                ('ctime', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('utime', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('product_line', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.Group', verbose_name='产品线')),
            ],
            options={
                'verbose_name': '数据库登陆用户',
                'verbose_name_plural': '数据库登陆用户',
                'db_table': 'db_user',
                'permissions': {('read_db_user', '只读系统登陆用户')},
            },
        ),
        migrations.AddField(
            model_name='db_mysql',
            name='db_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='db.db_user', verbose_name='数据库登陆用户'),
        ),
        migrations.AddField(
            model_name='db_mysql',
            name='product_line',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.Group', verbose_name='产品线'),
        ),
    ]

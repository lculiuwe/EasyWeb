# Generated by Django 2.1.3 on 2018-11-12 01:45

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='广告标题')),
                ('image', models.ImageField(blank=True, null=True, upload_to='ad_images', verbose_name='广告图片')),
                ('url', models.URLField(help_text='可以为本站URL地址或者外部网站地址！', verbose_name='链接地址')),
                ('index', models.IntegerField(default=1, verbose_name='顺序')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '广告轮播图',
                'verbose_name_plural': '广告轮播图',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='文章标题')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='文章内容')),
                ('abstract', models.CharField(blank=True, help_text='可选,如果为空则选取文章内容的前60个字符！', max_length=60, null=True, verbose_name='文章摘要')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_modified_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='浏览量')),
                ('likes', models.PositiveIntegerField(default=0, verbose_name='点赞数')),
                ('topped', models.BooleanField(default=False, verbose_name='是否置顶')),
                ('status', models.CharField(choices=[('d', 'Draft'), ('p', 'Published')], max_length=1, verbose_name='文章状态')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='文章类型')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_modified_time', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
            ],
            options={
                'verbose_name': '文章类型',
                'verbose_name_plural': '文章类型',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='标签名称')),
            ],
            options={
                'verbose_name': '标签名称',
                'verbose_name_plural': '标签名称',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.Category', verbose_name='文章分类'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, to='cms.Tag', verbose_name='文章标签'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-10-19 11:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0002_bookinfo_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atitle', models.CharField(max_length=20)),
                ('aparent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='booktest.AreaInfo')),
            ],
        ),
        migrations.CreateModel(
            name='NewsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ntitle', models.CharField(max_length=20)),
                ('npub_date', models.DateTimeField(auto_now_add=True)),
                ('ncontent', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=20)),
                ('sage', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StuInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scontent', models.CharField(max_length=200)),
                ('stu', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='booktest.Student')),
            ],
        ),
        migrations.CreateModel(
            name='TypeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tname', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('followers', models.ManyToManyField(related_name='_user_followers_+', to='booktest.User')),
            ],
        ),
        migrations.AddField(
            model_name='newsinfo',
            name='ntype',
            field=models.ManyToManyField(to='booktest.TypeInfo'),
        ),
    ]

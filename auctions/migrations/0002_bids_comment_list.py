# Generated by Django 3.2.5 on 2021-07-08 11:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.IntegerField(max_length=6)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentInput', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('desc', models.CharField(max_length=64)),
                ('price', models.IntegerField(max_length=6)),
                ('bids', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bidders', to='auctions.bids')),
                ('comments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='auctions.comment')),
            ],
        ),
    ]
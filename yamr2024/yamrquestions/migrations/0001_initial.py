# Generated by Django 5.0 on 2024-01-01 09:04

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='YamrQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('content', models.CharField(max_length=240)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yamr_questions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='YamrAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('yamrbody', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yamr_authored_answers', to=settings.AUTH_USER_MODEL)),
                ('voters', models.ManyToManyField(related_name='yamr_votes', to=settings.AUTH_USER_MODEL)),
                ('yamrquestion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yamr_answers', to='yamrquestions.yamrquestion')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

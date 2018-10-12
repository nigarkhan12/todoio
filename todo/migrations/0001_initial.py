# Generated by Django 2.0.8 on 2018-09-28 05:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('title_text', models.CharField(max_length=200)),
                ('reminder', models.DateTimeField(null=True)),
                ('notes', models.TextField(null=True)),
            ],
        ),
    ]

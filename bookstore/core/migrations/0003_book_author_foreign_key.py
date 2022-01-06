# Generated by Django 4.0.1 on 2022-01-06 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author_foreign_key',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.author'),
        ),
    ]
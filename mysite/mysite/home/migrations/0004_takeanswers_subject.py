# Generated by Django 5.0.6 on 2024-07-07 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_takeanswers_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='takeanswers',
            name='subject',
            field=models.CharField(default=1, max_length=5000),
            preserve_default=False,
        ),
    ]

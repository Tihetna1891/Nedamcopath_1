# Generated by Django 3.2.21 on 2023-10-04 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_rename_category_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('active', 'Active')], default='active', max_length=10),
        ),
    ]

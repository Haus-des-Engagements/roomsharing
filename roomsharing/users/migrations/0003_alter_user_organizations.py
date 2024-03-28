# Generated by Django 4.2.11 on 2024-03-28 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_organization_alter_user_options_remove_user_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='organizations',
            field=models.ManyToManyField(blank=True, related_name='users_of_organization', related_query_name='user_of_organization', to='users.organization', verbose_name='Organizations'),
        ),
    ]

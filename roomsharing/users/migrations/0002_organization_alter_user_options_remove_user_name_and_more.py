# Generated by Django 4.2.11 on 2024-03-26 05:15

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=160, verbose_name='Name')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name')),
                ('street', models.CharField(max_length=56, verbose_name='Street')),
                ('house_number', models.CharField(max_length=8, verbose_name='House Number')),
                ('zip_code', models.CharField(max_length=12, verbose_name='Zip Code')),
                ('city', models.CharField(max_length=24, verbose_name='City')),
            ],
            options={
                'verbose_name': 'Organization',
                'verbose_name_plural': 'Organizations',
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['email'], 'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='John', verbose_name='First Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='Doe', verbose_name='Last Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='organizations',
            field=models.ManyToManyField(blank=True, related_name='user_of_organizations', related_query_name='users_of_organizations', to='users.organization', verbose_name='Organizations'),
        ),
    ]

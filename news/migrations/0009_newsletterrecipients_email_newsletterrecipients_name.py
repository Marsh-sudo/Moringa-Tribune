# Generated by Django 4.0.3 on 2022-03-29 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_alter_article_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletterrecipients',
            name='email',
            field=models.EmailField(default='default', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newsletterrecipients',
            name='name',
            field=models.CharField(default='string', max_length=20),
            preserve_default=False,
        ),
    ]

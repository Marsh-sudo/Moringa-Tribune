# Generated by Django 4.0.3 on 2022-03-28 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_remove_newsletterrecipients_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=60),
        ),
    ]
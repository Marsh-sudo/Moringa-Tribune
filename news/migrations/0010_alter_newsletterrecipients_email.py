# Generated by Django 4.0.3 on 2022-03-29 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_newsletterrecipients_email_newsletterrecipients_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletterrecipients',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]

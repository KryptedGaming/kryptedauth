# Generated by Django 2.0.2 on 2018-03-18 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_grouprequest_processed_by'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grouprequest',
            options={'permissions': (('manage_group_requests', 'Can manage group requests.'), ('audit_group_requests', 'Can view the group request audit log.'))},
        ),
    ]
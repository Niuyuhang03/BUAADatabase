# Generated by Django 2.1.2 on 2018-12-11 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='addrid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='orderlist',
            name='orderid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='picture',
            name='picid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='telephone',
            name='teleid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='ticketid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='userid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
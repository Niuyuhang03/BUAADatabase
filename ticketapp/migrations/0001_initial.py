# Generated by Django 2.1.2 on 2018-12-14 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='address',
            fields=[
                ('addrid', models.AutoField(primary_key=True, serialize=False)),
                ('addrinfo', models.CharField(max_length=40)),
                ('userid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='orderlist',
            fields=[
                ('orderid', models.AutoField(primary_key=True, serialize=False)),
                ('ordertime', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='picture',
            fields=[
                ('picid', models.AutoField(primary_key=True, serialize=False)),
                ('picpath', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='telephone',
            fields=[
                ('teleid', models.AutoField(primary_key=True, serialize=False)),
                ('teleinfo', models.CharField(max_length=40)),
                ('userid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ticket',
            fields=[
                ('ticketid', models.AutoField(primary_key=True, serialize=False)),
                ('ticketname', models.CharField(max_length=40)),
                ('ticketlocation', models.CharField(max_length=40)),
                ('tickettime', models.CharField(max_length=40)),
                ('ticketinfo', models.CharField(max_length=200)),
                ('ticketprice', models.IntegerField()),
                ('ticketstatus', models.IntegerField(default=0)),
                ('ticketimg', models.CharField(default='0.JPG', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ticket_order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticketid', models.IntegerField()),
                ('orderid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('userid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20, unique=True)),
                ('usersex', models.CharField(max_length=2)),
                ('userpwd', models.CharField(max_length=20)),
                ('userimg', models.CharField(default='0.JPG', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='user_order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField()),
                ('orderid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='user_ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField()),
                ('ticketid', models.IntegerField()),
            ],
        ),
    ]

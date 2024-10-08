# Generated by Django 3.1.1 on 2023-11-07 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_auto_20220205_0503'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('photo_service', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('service_type', models.CharField(choices=[('home_loan', 'Home Loan'), ('interior_design', 'Interior Design'), ('building_materials', 'Building Materials'), ('personal_loan', 'Personal Loan'), ('house_design', 'House Design'), ('building_contractor', 'Building Contractor')], max_length=50)),
                ('contact_email', models.EmailField(blank=True, max_length=254)),
                ('contact_phone', models.IntegerField()),
            ],
        ),
    ]

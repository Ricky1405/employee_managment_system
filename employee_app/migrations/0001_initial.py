# Generated by Django 5.1.4 on 2024-12-11 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('f_Id', models.AutoField(primary_key=True, serialize=False)),
                ('f_Image', models.ImageField(upload_to='employee_images/')),
                ('f_Name', models.CharField(max_length=100)),
                ('f_Email', models.EmailField(max_length=254, unique=True)),
                ('f_Mobile', models.CharField(max_length=15)),
                ('f_Designation', models.CharField(max_length=100)),
                ('f_gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('f_Course', models.CharField(max_length=100)),
                ('f_Createdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('f_sno', models.AutoField(primary_key=True, serialize=False)),
                ('f_userName', models.CharField(max_length=150, unique=True)),
                ('f_Pwd', models.CharField(max_length=100)),
            ],
        ),
    ]
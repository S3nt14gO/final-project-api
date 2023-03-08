# Generated by Django 4.1.6 on 2023-03-08 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='RegisterFreelancer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=False)),
                ('phone_number', models.CharField(max_length=11)),
                ('password', models.CharField(max_length=300)),
                ('overview', models.CharField(max_length=500)),
                ('user_image', models.ImageField(upload_to='static_dirs/images/user_image')),
                ('street_address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('postal_code', models.CharField(max_length=20)),
                ('education', models.ManyToManyField(to='authentication.education')),
                ('experience', models.ManyToManyField(to='authentication.experience')),
                ('job_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.jobtitle')),
                ('services', models.ManyToManyField(to='authentication.services')),
                ('skills', models.ManyToManyField(to='authentication.skills')),
            ],
        ),
    ]
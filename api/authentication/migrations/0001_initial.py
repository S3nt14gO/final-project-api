

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=50)),
                ('degree', models.CharField(max_length=100)),
                ('study', models.CharField(max_length=100)),
                ('from_year', models.IntegerField(verbose_name=4)),
                ('to_year', models.IntegerField(verbose_name=4)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=200)),
                ('is_current_work_in_company', models.BooleanField(default=False)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(

            name='RegisterUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=70)),
                ('password', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to='static_dirs/images/user_image')),
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
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.categoryservice')),
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

                ('job_title', models.CharField(max_length=300, null=True)),
                ('overview', models.CharField(max_length=500, null=True)),
                ('user_image', models.ImageField(null=True, upload_to='static_dirs/images/user_image')),
                ('street_address', models.CharField(max_length=50, null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('state', models.CharField(max_length=50, null=True)),
                ('postal_code', models.CharField(max_length=20, null=True)),
                ('education', models.ManyToManyField(null=True, to='authentication.education')),
                ('experience', models.ManyToManyField(null=True, to='authentication.experience')),
                ('services', models.ManyToManyField(null=True, to='authentication.services')),
                ('skills', models.ManyToManyField(null=True, to='authentication.skills')),
            ],
        ),
    ]

from django.db import models

# Create your models here.
class CategoryService (models.Model):
    id = models.AutoField
    name = models.CharField(max_length=50)

class Services (models.Model):
    id = models.AutoField
    name = models.CharField(max_length=50)
    category_service = models.ForeignKey(CategoryService, on_delete=models.CASCADE)


class Experience (models.Model):
    title = models.CharField(max_length=50)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    is_current_work_in_company = models.BooleanField(default=False)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.CharField(max_length=500)
    id = models.AutoField

    


class Education (models.Model):
    school = models.CharField(max_length=50)
    degree = models.CharField(max_length=100)
    study = models.CharField(max_length=100)
    from_year = models.IntegerField(4)
    to_year = models.IntegerField(4)
    description = models.CharField(max_length=500)
    id = models.AutoField
class Skills(models.Model):
    name=models.CharField(max_length=50)
    id=models.AutoField


class RegisterFreelancer(models.Model):
    id = models.AutoField
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    is_active=models.BooleanField(default=False)
    phone_number=models.CharField(max_length=11)
    password=models.CharField(max_length=300)
    job_title=models.CharField(null=True,max_length=300)
    overview=models.CharField(max_length=500,null=True)
    user_image=models.ImageField(upload_to='static_dirs/images/user_image',null=True,)
    street_address=models.CharField(max_length=50,null=True,)
    city=models.CharField(max_length=50,null=True,)
    state=models.CharField(max_length=50,null=True,)
    postal_code=models.CharField(max_length=20,null=True,)
    experience=models.ManyToManyField(Experience,null=True,)
    education=models.ManyToManyField(Education,null=True,)
    skills=models.ManyToManyField(Skills,null=True,)
    services=models.ManyToManyField(Services,null=True,)
    is_complete_date=models.BooleanField(default=False)

class RegisterUser(models.Model):
    id = models.AutoField
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    phone=models.CharField(max_length=11)
    email=models.EmailField(max_length=70)
    password=models.CharField(max_length=100)
    is_active=models.BooleanField(default=False)
    image=models.ImageField(upload_to='static_dirs/images/user_image')


class Certifications(models.Model):
    id = models.AutoField
    certifications_freelancer = models.ForeignKey(RegisterFreelancer, on_delete=models.CASCADE)
    provider=models.CharField(max_length=50)
    description=models.CharField(max_length=500)
    Issue_date= models.DateField()
    Expiration_date= models.DateField()
    Certification_ID=models.CharField(max_length=50)
    Certification_UR=models.CharField(max_length=100)


class CertificationType(models.Model):
    id = models.AutoField
    name=models.CharField(max_length=50)


class WorkHistory(models.Model):
    id = models.AutoField
    work_history_freelancer = models.ForeignKey(RegisterFreelancer, on_delete=models.CASCADE)
    location=models.CharField(max_length=100)
    date= models.DateField()
    const=models.DecimalField(decimal_places=10,max_digits=12)


class ImagesProject(models.Model):
    id = models.AutoField
    image_project = models.ImageField(upload_to='static_dirs/images/project_image')

class Portfilo(models.Model):
    id = models.AutoField
    portfilo_freelancer = models.ForeignKey(RegisterFreelancer, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    images = models.ManyToManyField(ImagesProject,null=True,)
    linkVide= models.URLField(max_length=200)
    description=models.CharField(max_length=50)









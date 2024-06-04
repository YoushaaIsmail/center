from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django_resized import ResizedImageField
import os
def upload_to(inst,filename):
      base_path="profile"
      safe_filename=str(filename)
      final_path=os.path.join(base_path,safe_filename)
      return final_path
class User(AbstractUser):
           list1=(
            ('male', 'male'),
            ('female', 'female'),
)
           list2=(
            ('Patient', 'Patient'),
            ('Manager', 'Manager'),
            ('Recption', 'Recption')
)
           email=models.EmailField(unique=True)
           phone=models.CharField(max_length=15,null=True)
           name=models.CharField(max_length=30)
           photo=ResizedImageField(upload_to=upload_to,null=True,blank=True)
           address=models.CharField(max_length=30,null=True)
           birthday=models.DateField(null=True)
           gender=models.CharField(max_length=20,choices=list1,null=True)
           type=models.CharField(max_length=20,choices=list2,null=True)

           USERNAME_FIELD='email'
           REQUIRED_FIELDS=[]
           def __str__(self):
               return self.email

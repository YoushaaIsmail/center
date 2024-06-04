from django.db import models
from django_resized import ResizedImageField
import os
from User.models import User
from random import randint
# Create your models here.
def upload_to(inst,filename):
      base_path="profile"
      safe_filename=str(filename)
      final_path=os.path.join(base_path,safe_filename)
      return final_path

class Section(models.Model):
   Img1=ResizedImageField(upload_to=upload_to,null=True,blank=True)
   fullname=models.CharField(max_length=100)
   name=models.CharField(max_length=100)

class Employ(models.Model):
   name=models.CharField(max_length=100)
   specialization=models.CharField(max_length=100)
   Des=models.CharField(max_length=300)
   Img1=ResizedImageField(upload_to='profile/',null=True,blank=True)

class Doctor(Employ):
    price=models.FloatField()
    section=models.ForeignKey(Section,on_delete=models.CASCADE,related_name='Doctor_Section')
   
class Daywork(models.Model):
    listt1=(
       (4, 'Friday'),
       (5, 'Saturday'),
       (6, 'Sunday'),
      (0, 'Monday'),
      (1,'Tuesday'),
      (2,'Wednesday'),
      (3,'Thursday')
)
        
    code=models.IntegerField(choices=listt1)
    startwork=models.TimeField()
    endwork=models.TimeField()
    Employ=models.ForeignKey(Employ,on_delete=models.CASCADE,related_name='Day_Employee')


class News(models.Model):
    name=models.CharField(max_length=15)
    Des=models.CharField(max_length=300)
    Img1=ResizedImageField(upload_to=upload_to,null=True,blank=True)
    date=models.DateTimeField(auto_created=True,blank=True,null=True)

class Clinic(models.Model):
    Img1=ResizedImageField(upload_to=upload_to,null=True,blank=True)
    name=models.CharField(max_length=30)
    floorNumber=models.IntegerField()
    idRoomNumber=models.IntegerField()

class Therapist(Employ):

   service=models.ForeignKey(Clinic,on_delete=models.CASCADE,related_name='therapist_clinic')

class offer(models.Model):
     Img1=ResizedImageField(upload_to=upload_to,null=True,blank=True)
     name=models.CharField(max_length=15)
     oldprice=models.FloatField()
     discount=models.FloatField()
     doctor=models.ForeignKey(Therapist,on_delete=models.CASCADE,related_name='offer_Therapist')
     sevice=models.ForeignKey(Clinic,on_delete=models.CASCADE,related_name='offer_sevice')
     date=models.DateField()
     durtion=models.IntegerField()




class Device(models.Model):
    price=models.FloatField()
    name=models.CharField(max_length=15)
    Des=models.CharField(max_length=300)  
    Img1=ResizedImageField(upload_to=upload_to,null=True,blank=True)
    service=models.ForeignKey(Clinic,on_delete=models.CASCADE,related_name='Device_clinic')



class AppointmentDoctor(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE,related_name='Appointment_Doctor')
    patient=models.ForeignKey(User,on_delete=models.CASCADE,related_name='AppointmentDoctor_patient')
    Date=models.DateField()
    time=models.TimeField()

class Appointmentclinic(models.Model):
    device=models.ForeignKey(Device,on_delete=models.CASCADE,related_name='Appointmentservice_Device')
    patient=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Appointmentservice_patient')
    therapist=models.ForeignKey(Therapist,on_delete=models.CASCADE,related_name='Appointmentservice_therapist')
    Date=models.DateField()
    time=models.TimeField()

class FaDoctor(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE,related_name='faDoctor_Doctor')
    patient=models.ForeignKey(User,on_delete=models.CASCADE,related_name='faDoctor_patient')

class Faclinic(models.Model):
    clinic=models.ForeignKey(Clinic,on_delete=models.CASCADE,related_name='faclinic_clinic')
    patient=models.ForeignKey(User,on_delete=models.CASCADE,related_name='faclinic_patient')

class likenews(models.Model):
    new=models.ForeignKey(News,on_delete=models.CASCADE,related_name='likenews_news')
    patient=models.ForeignKey(User,on_delete=models.CASCADE,related_name='likenews_patient')
 
class location(models.Model):
    country=models.CharField(max_length=30)
    lat=models.CharField(max_length=30)
    long=models.CharField(max_length=30)

class about(models.Model):
    whatsapp=models.CharField(max_length=30) 
    youtube=models.CharField(max_length=30)
    Instagram=models.CharField(max_length=30)
    fasebook=models.CharField(max_length=30)            
    loction=models.OneToOneField(location,on_delete=models.CASCADE,related_name='loction_about')

class comentClinie(models.Model):  
    clinic=models.ForeignKey(Clinic,on_delete=models.CASCADE,related_name='COclinic_clinic')
    patient=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Coclinic_patient')  
    Des=models.CharField(max_length=100)

class comentNews(models.Model):  
    new=models.ForeignKey(News,on_delete=models.CASCADE,related_name='CONew')
    patient=models.ForeignKey(User,on_delete=models.CASCADE,related_name='CoNews_patient')  
    Des=models.CharField(max_length=100)

class ratingClinie(models.Model):  
    clinic=models.ForeignKey(Clinic,on_delete=models.CASCADE,related_name='Raclinic_clinic')
    patient=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Raclinic_patient')  
    scoure=models.FloatField()   

class Fathei(models.Model):
    therapist=models.ForeignKey(Therapist,on_delete=models.CASCADE,related_name='fathe_the')
    patient=models.ForeignKey(User,on_delete=models.CASCADE,related_name='fapatient_th')    
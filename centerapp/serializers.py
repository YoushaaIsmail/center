from rest_framework import serializers
from .models import *
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import MinValueValidator, MaxValueValidator
from random import randint
import random
from django.conf import settings

class rating():
    def __init__(self):
        self.rate = random.randint(0, 5)
        self.count = random.randint(500, 1000)


class newaSreializes(serializers.ModelSerializer):
    Numbercomment = serializers.SerializerMethodField('get_account')
    Img1 = serializers.SerializerMethodField('get_image_url')
    Numberlike= serializers.SerializerMethodField('numberLike')
    likebool = serializers.SerializerMethodField('get_is_like')
    def get_is_like(self, obj):
        request = self.context.get('request', None)
        if request and request.user.is_authenticated:
            if likenews.objects.filter(new=obj, patient=request.user).exists():
                return True
        return False
    def numberLike(self, obj):
        if obj:
            LN=likenews.objects.filter(new=obj).count()
            return LN
        return 0 
    def get_account(self, obj):
        if obj:
            o = randint(1000, 1500)
            return o
        return None

    def get_image_url(self, obj):
        if obj.Img1:
            return self.context['request'].build_absolute_uri(obj.Img1.url)
        return None

    class Meta:
        model = News
        fields = '__all__'

class TherapistSreializes(serializers.ModelSerializer):
    class Meta:
        model = Therapist
        fields='__all__'

class seviceSreializes(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields='__all__'
class DevSreializes(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields='__all__'
class seviceSreializesapi(serializers.ModelSerializer):
    Numbercomment = serializers.SerializerMethodField('get_Numbercomment')
    doctors=serializers.SerializerMethodField('get_Doctos')
    devices=serializers.SerializerMethodField('get_devices')
    favbool = serializers.SerializerMethodField('get_is_favorited')
    Img1 = serializers.SerializerMethodField('get_image_url')
    number_doctor =serializers.SerializerMethodField('get_number_doctor')
    number_device =serializers.SerializerMethodField('get_number_device')  
    rating  =serializers.SerializerMethodField('get_rate')  
    def get_Numbercomment(self, obj):
        if obj:
            SC=0
            SC=comentClinie.objects.filter(clinic=obj).count()
            return SC
        return None
    def get_devices(self, obj):
        if obj:
            dev=[]
            devices=Device.objects.filter(service=obj).all()
            print(devices)
            for i in devices:
               div_ser=DevSreializes(i)
               se_data = div_ser.data
               se_data['Img1'] = self.context['request'].build_absolute_uri(i.Img1.url)
               dev.append(se_data)
            return dev  
    def get_Doctos(self, obj):
        if obj:
            dev=[]
            the=Therapist.objects.filter(service=obj).all()

            for i in the:
               request = self.context.get('request', None)
               div_ser=TherapistSreializes(i)
               se_data = div_ser.data
               if request and request.user.is_authenticated:
                   if Fathei.objects.filter(therapist=i, patient=request.user).exists():
                       se_data['IS_favourit']=True
                   else: 
                       se_data['IS_favourit']=False   

               se_data['Img1'] = self.context['request'].build_absolute_uri(i.Img1.url)
               
               dev.append(se_data)
            return dev      
        return None

    def get_rate(self, obj):
        if obj:
           r = rating()
           NB=ratingClinie.objects.filter(clinic=obj).count()
           RC=ratingClinie.objects.filter(clinic=obj)
           if NB and RC:
               i=0
               for j in RC:
                   i =i+j.scoure

                   return {'rate': i/NB, 'count': NB} 
           return None   
    def get_image_url(self, obj):
        if obj.Img1:
            return self.context['request'].build_absolute_uri(obj.Img1.url)
        return None

    class Meta:
        model = Clinic
        fields = '__all__'

    def get_is_favorited(self, obj):
        request = self.context.get('request', None)
        if request and request.user.is_authenticated:
            if Faclinic.objects.filter(clinic=obj, patient=request.user).exists():
                return True
        return False
    def get_number_doctor(self, obj):
        if obj:
            the=Therapist.objects.filter(service=obj).count()
            return the
        return 0
    def get_number_device(self, obj):
        if obj:
            the=Device.objects.filter(service=obj).count()
            return the
        return 0
        
class offerSreializes(serializers.ModelSerializer):
    Newprice = serializers.SerializerMethodField('newprice')
    Img1 = serializers.SerializerMethodField('get_image_url')
    doctor = serializers.SerializerMethodField('get_doctor')
    sevice= serializers.SerializerMethodField('get_service')

    def get_service(self, obj):
        if obj.doctor:
            servic_serializer = seviceSreializes(obj.sevice)
            se_data = servic_serializer.data
            if obj.sevice.Img1:
                se_data['Img1'] = self.context['request'].build_absolute_uri(obj.sevice.Img1.url)
            return se_data
        return None

    def get_doctor(self, obj):
        if obj.doctor:
            therapist_serializer = TherapistSreializes(obj.doctor)
            therapist_data = therapist_serializer.data
            if obj.doctor.Img1:
                therapist_data['Img1'] = self.context['request'].build_absolute_uri(obj.doctor.Img1.url)
            return therapist_data
        return None

    def newprice(self, obj):
        if obj:
            p = obj.oldprice - (obj.oldprice * (obj.discount / 100))
            return p
        return None

    def get_image_url(self, obj):
        if obj.Img1:
            return self.context['request'].build_absolute_uri(obj.Img1.url)
        return None
    class Meta:
        model = offer
        fields = ['name','oldprice','doctor', 'Img1','sevice','date','durtion','discount','Newprice']
class doctorSerSreializes(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields ='__all__'
class sectionSerSreializes(serializers.ModelSerializer):
    number_doctor =serializers.SerializerMethodField('get_number_doctor')
    doctors=serializers.SerializerMethodField('get_Doctos')    
    def get_Doctos(self, obj):
        if obj:
            dev=[]
            doc=Doctor.objects.filter(section=obj).all()

            for i in doc:
               request = self.context.get('request', None)
               div_ser=doctorSerSreializes(i)
               se_data = div_ser.data
               if request and request.user.is_authenticated:
                   if FaDoctor.objects.filter(doctor=i, patient=request.user).exists():
                       se_data['IS_favourit']=True
                   else: 
                       se_data['IS_favourit']=False   

               se_data['Img1'] = self.context['request'].build_absolute_uri(i.Img1.url)
               
               dev.append(se_data)
            return dev      
        return None
    def get_number_doctor(self, obj):
        if obj:
            doc=Doctor.objects.filter(section=obj).count()
            return doc
        return 0
    class Meta:
        model = Section
        fields ='__all__'

class appcliSerSreializes(serializers.ModelSerializer):
    class Meta:
        model = Appointmentclinic
        fields ='__all__'

class appdocSerSreializes(serializers.ModelSerializer):
    class Meta:
        model = AppointmentDoctor
        fields ='__all__'     

class likenewsSerSreializes(serializers.ModelSerializer):
    class Meta:
        model = likenews
        fields ='__all__'      

class FaDoSerSreializes(serializers.ModelSerializer):
    class Meta:
        model = FaDoctor
        fields ='__all__'      

class FaCliSerSreializes(serializers.ModelSerializer):
    class Meta:
        model = Faclinic
        fields ='__all__'  


class FaTheSerSreializes(serializers.ModelSerializer):
    class Meta:
        model = Fathei
        fields ='__all__'                   


class CoCliSerSreializes(serializers.ModelSerializer):
    class Meta:
        model = comentClinie
        fields ='__all__'                   

class CoNewsSerSreializes(serializers.ModelSerializer):
    class Meta:
        model = comentNews
        fields ='__all__' 

class RaCliSerSreializes(serializers.ModelSerializer):
    class Meta:
        model = ratingClinie
        fields ='__all__'                   

class LocationSerSreializes(serializers.ModelSerializer):
    class Meta:
        model = location
        fields ='__all__'                   

class aboutSerSreializes(serializers.ModelSerializer):
    loction=serializers.SerializerMethodField('get_location')
    def get_location(self, obj):
        if obj.loction:

            return LocationSerSreializes(obj.loction).data
        else:
            return None
    class Meta:
        model = about
        fields ='__all__'                           


class appcliSerSreializes2(serializers.ModelSerializer):
    doctor=serializers.SerializerMethodField('get_Doctos')    
    def get_Doctos(self, obj):
        if obj:
            se_data=doctorSerSreializes(obj.doctor).data
            se_data['Img1'] = self.context['request'].build_absolute_uri(obj.doctor.Img1.url)
            return se_data
    class Meta:
        model = Appointmentclinic
        fields ='__all__'

class appdocSerSreializes1(serializers.ModelSerializer):
    doctor=serializers.SerializerMethodField('get_Doctos')    
    def get_Doctos(self, obj):
        if obj:
            se_data=doctorSerSreializes(obj.doctor).data
            se_data['Img1'] = self.context['request'].build_absolute_uri(obj.doctor.Img1.url)
            return se_data
    class Meta:
        model = AppointmentDoctor
        fields ='__all__'         

class doSeSerSreializes1(serializers.ModelSerializer):

    class Meta:
        model = Section
        fields ='__all__'        

class doctorSerSreializes1(serializers.ModelSerializer):
    Img1 = serializers.SerializerMethodField('get_image_url')
    section=serializers.SerializerMethodField('get_section')
    def get_image_url(self, obj):
        if obj.Img1:
                if obj.Img1:
                    return self.context['request'].build_absolute_uri(obj.Img1.url)
                return obj.Img1
        return None
    def get_section(self, obj):
        if obj.section:
            return doSeSerSreializes1(obj.section).data
        return None
    class Meta:
        model = Doctor
        fields ='__all__'        

class TherapistSreializes1(serializers.ModelSerializer):
    service=serializers.SerializerMethodField('get_service')
    def get_service(self, obj):
        if obj.service:
            return seviceSreializes(obj.service).data
        return None
    class Meta:
        model = Therapist
        fields='__all__'        

class DevSreializes1(serializers.ModelSerializer):
    service=serializers.SerializerMethodField('get_service')
    def get_service(self, obj):
        if obj.service:
            return seviceSreializes(obj.service).data
        return None
    class Meta:
        model = Device
        fields='__all__'        

class FaDoSerSreializes1(serializers.ModelSerializer):
    doctor=serializers.SerializerMethodField('get_doctor')
    def get_doctor(self, obj):
        if obj.doctor:
            return doctorSerSreializes(obj.doctor).data
        return None
    class Meta:
        model = FaDoctor
        fields ='__all__'          
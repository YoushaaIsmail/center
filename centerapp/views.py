from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework import status
from dj_rest_auth.views import LoginView
from rest_framework.decorators import api_view
from .models import *
from .serializers import * 
from User.models import User
from django.http import JsonResponse
from datetime import datetime, timedelta, time
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.

# class NewloginView(LoginView):
#     def get_response(self):
#         response = super().get_response()

#         if response.status_code == status.HTTP_200_OK:
#             user = self.user
#             if user.is_verified:
#                 token = response.data['key']
#                 return Response({
#                     'status': status.HTTP_200_OK,
#                     'message': 'Login successful',
#                     'data': {
#                         'key': token
#                     }
#                 })
#             else:
#                 return Response({
#                     'status': status.HTTP_401_UNAUTHORIZED,
#                     'message': 'User is not verified',
#                     'data': None
#                 })
#         return response
@api_view(['GET'])
def getadvice(request):
    news = News.objects.all()
    serializer = newaSreializes(news, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def getaboutapi(request):
    about1 = about.objects.all()
    serializer = aboutSerSreializes(about1, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def getofferapi(request):
    off = offer.objects.all()
    serializer = offerSreializes(off, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def getservice(request):
    print(request.data)
    ser = Clinic.objects.all()
    serializer = seviceSreializesapi(ser, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def getsectionapi(request):
    print(request.data)
    ser = Section.objects.all()
    serializer = sectionSerSreializes(ser, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def getMyFaDo(request):
    print(request.data)
    ser = FaDoctor.objects.filter(patient=request.user)
    serializer = FaDoSerSreializes1(ser, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def getMyFaCl(request):
    print(request.data)
    ser = Faclinic.objects.filter(patient=request.user)
    serializer = FaCliSerSreializes(ser, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def getcommentCli(request,idCl):
    ser = comentClinie.objects.filter(clinic=idCl)
    serializer = CoCliSerSreializes(ser, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def getcommentNew(request,idNe):
    ser = comentNews.objects.filter(new=idNe)
    serializer = CoNewsSerSreializes(ser, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def getMyFaThe(request):
    print(request.data)
    ser = Fathei.objects.filter(patient=request.user)
    serializer = FaTheSerSreializes(ser, many=True, context={'request': request})
    return Response(serializer.data)
from django.db.models import Q
@api_view(['GET'])
def getMyApDoAfter(request):
    print(request.data)
    ser = AppointmentDoctor.objects.filter(
    Q(patient=request.user) &
    Q(Date__gt=datetime.now().date())
)
    serializer = appdocSerSreializes1(ser, many=True, context={'request': request})
    return Response(serializer.data)
@api_view(['GET'])
def getMyApDoBefor(request):
    print(request.data)
    ser = AppointmentDoctor.objects.filter(
    Q(patient=request.user) &
    Q(Date__lt=datetime.now().date())
)
    serializer = appdocSerSreializes1(ser, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def getMyApClAfter(request):
    print(request.data)
    ser = Appointmentclinic.objects.filter(
    Q(patient=request.user) &
    Q(Date__gt=datetime.now().date())
)
    serializer = appcliSerSreializes2(ser, many=True, context={'request': request})
    return Response(serializer.data)
@api_view(['GET'])
def getMyApClBefor(request):
    print(request.data)
    ser = Appointmentclinic.objects.filter(
    Q(patient=request.user) &
    Q(Date__lt=datetime.now().date())
)
    serializer = appcliSerSreializes2(ser, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def getsearchClinic(request,Nclinic):
    
    ser = Clinic.objects.filter(name=Nclinic)

    serializer = seviceSreializesapi(ser, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def searchDoctor(request,Ndoctor):
    
    ser = Doctor.objects.filter(name=Ndoctor)

    serializer = doctorSerSreializes1(ser, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def getfiltersection(request,Nseaction):
    
    ser = Section.objects.filter(name=Nseaction)

    serializer = sectionSerSreializes(ser, many=True, context={'request': request})
    return Response(serializer.data)
@api_view(['GET'])
def getsearchThr(request,NThe):
    
    ser = Therapist.objects.filter(name=NThe)

    serializer = TherapistSreializes1(ser, many=True, context={'request': request})
    return Response(serializer.data)
@api_view(['GET'])
def getsearchDev(request,NDev):
    
    ser = Device.objects.filter(name=NDev)

    serializer = DevSreializes1(ser, many=True, context={'request': request})
    return Response(serializer.data)
@api_view(['POST'])
def getappiontmenyclinicapi(request):
    av_app_date = []
    lav_app_date = []
    try:
     data = request.data
     idDev=data['idDev']
     idDoc=data['idDoc']

     the=Therapist.objects.get(id=idDoc)


     if idDev and idDoc:
      appointments=[]
      print(idDoc)
      current_date = datetime.now().date()

      day = Daywork.objects.filter(Employ=idDoc).all()
      for l in range(4):
       for i in day:
        if i.code==0:
            dayname="Monday"
        if i.code==1:
            dayname="Tuesday"
        if i.code==2:
            dayname="Wednesday"
        if i.code==3:
            dayname="Thursday"
        if i.code==4:
            dayname="Friday"
        if i.code==5:
            dayname="Saturday"
        if i.code==6:
            dayname="Sunday"                                                                        
        next_day = current_date + timedelta(days=((i.code - current_date.weekday()) % 7)+7*l)

        appointments = Appointmentclinic.objects.filter(therapist=idDoc, Date=next_day).order_by('time')
       
        
        start_datetime = datetime.combine(next_day, i.startwork)
        final_datetime = datetime.combine(next_day, i.endwork)        
        finalapppiont = datetime.combine(next_day, time(hour=0, minute=0, second=0))
        finalapppiont1 = datetime.combine(next_day, time(hour=0, minute=0, second=0))
        if appointments:
          for j in appointments:
            finalapppiont=datetime.combine(next_day, j.time)

            j_datetime = datetime.combine(next_day, j.time)  
            print(start_datetime)
            print(j_datetime)
            if j_datetime >= start_datetime + timedelta(minutes=30):
                print('i')
                
                y = f"{dayname},{next_day.strftime('%Y-%m-%d')}/{start_datetime.strftime('%H:%M:%S')},{j_datetime.strftime('%H:%M:%S')}"
                av_app_date.append(y)
                start_datetime = j_datetime + timedelta(minutes=30) 
            else:
                start_datetime = start_datetime+ timedelta(minutes=30) 

          y = f"{dayname},{next_day.strftime('%Y-%m-%d')}/{(finalapppiont+ timedelta(minutes=30)).strftime('%H:%M:%S')},{final_datetime.strftime('%H:%M:%S')}"
          av_app_date.append(y)
        else:
              y = f"{dayname},{next_day.strftime('%Y-%m-%d')}/{i.startwork.strftime('%H:%M:%S')},{i.endwork.strftime('%H:%M:%S')}"
              av_app_date.append(y)   
      print(av_app_date)                    
      for k in av_app_date:
            p1,p2=k.split('/')
          

            dname,date_str= p1.split(',')
            start_time_str, end_time_str = p2.split(',')            

            date = datetime.strptime(date_str, '%Y-%m-%d').date()
            start_datetime = datetime.strptime(start_time_str, '%H:%M:%S')
            end_datetime = datetime.strptime(end_time_str, '%H:%M:%S')
            appointments2 = Appointmentclinic.objects.filter(device=idDev, Date=date).order_by('time')
            
            while end_datetime >= start_datetime + timedelta(minutes=30):
                t=None
                t=appointments2.filter(time=start_datetime).first()
                if t==None:

                  y = f"{dname},{date.strftime('%Y-%m-%d')}/{start_datetime.strftime('%H:%M:%S')},{(start_datetime + timedelta(minutes=30)).strftime('%H:%M:%S')}"
                  print(y)
                  lav_app_date.append(y)
                start_datetime = start_datetime + timedelta(minutes=30) 
                
      test1 = []  # Initialize the outer list
      i = 0  # Initialize the outer loop index

      while i < len(lav_app_date):
          test = []
          t1 = lav_app_date[i].split('/')[0]
          print(i)

          j = i
          while j < len(lav_app_date) and lav_app_date[j].split('/')[0] == t1:
              test.append(lav_app_date[j].split('/')[1])
              j += 1

          newdate = {
              'Day': t1,
              'time_sort': test
          }
          test1.append(newdate)

          i = j

      print(test1)
      return Response(test1)

                  
    except Exception as e:
            print(e)
@api_view(['POST'])
def getappintmentdoctorapi(request):
    av_app_date = []
    lav_app_date = []
    try:
     data = request.data
     idDoc=data['idDoc']

     doctor1=Doctor.objects.get(id=idDoc)


     if idDoc:
      print(idDoc)
      current_date = datetime.now().date()

      day = Daywork.objects.filter(Employ=idDoc).all()
      for l in range(4):
       for i in day:
        if i.code==0:
            dayname="Monday"
        if i.code==1:
            dayname="Tuesday"
        if i.code==2:
            dayname="Wednesday"
        if i.code==3:
            dayname="Thursday"
        if i.code==4:
            dayname="Friday"
        if i.code==5:
            dayname="Saturday"
        if i.code==6:
            dayname="Sunday"                                                                        
        next_day = current_date + timedelta(days=((i.code - current_date.weekday()) % 7)+7*l)

        appointments = AppointmentDoctor.objects.filter(doctor=idDoc, Date=next_day).order_by('time')


        
        start_datetime = datetime.combine(next_day, i.startwork)
        final_datetime = datetime.combine(next_day, i.endwork)        
        finalapppiont = datetime.combine(next_day, time(hour=0, minute=0, second=0))
        finalapppiont1 = datetime.combine(next_day, time(hour=0, minute=0, second=0))
        if appointments:
          for j in appointments:
            finalapppiont=datetime.combine(next_day, j.time)

            j_datetime = datetime.combine(next_day, j.time)  
            print(start_datetime)
            print(j_datetime)
            if j_datetime >= start_datetime + timedelta(minutes=30):
                print('i')
                
                y = f"{dayname},{next_day.strftime('%Y-%m-%d')}/{start_datetime.strftime('%H:%M:%S')},{j_datetime.strftime('%H:%M:%S')}"
                av_app_date.append(y)
                start_datetime = j_datetime + timedelta(minutes=30) 
            else:
                start_datetime = start_datetime+ timedelta(minutes=30) 

          y = f"{dayname},{next_day.strftime('%Y-%m-%d')}/{(finalapppiont+ timedelta(minutes=30)).strftime('%H:%M:%S')},{final_datetime.strftime('%H:%M:%S')}"
          av_app_date.append(y)
        else:
              y = f"{dayname},{next_day.strftime('%Y-%m-%d')}/{i.startwork.strftime('%H:%M:%S')},{i.endwork.strftime('%H:%M:%S')}"
              av_app_date.append(y)   
      print(av_app_date)                    
      for k in av_app_date:
            p1,p2=k.split('/')
          

            dname,date_str= p1.split(',')
            start_time_str, end_time_str = p2.split(',')            

            date = datetime.strptime(date_str, '%Y-%m-%d').date()
            start_datetime = datetime.strptime(start_time_str, '%H:%M:%S')
            end_datetime = datetime.strptime(end_time_str, '%H:%M:%S')

            while end_datetime >= start_datetime + timedelta(minutes=30):
                y = f"{dname},{date.strftime('%Y-%m-%d')}/{start_datetime.strftime('%H:%M:%S')},{(start_datetime + timedelta(minutes=30)).strftime('%H:%M:%S')}"
                print(y)
                lav_app_date.append(y)
                start_datetime = start_datetime + timedelta(minutes=30) 
                
      test1 = []  # Initialize the outer list
      i = 0  # Initialize the outer loop index

      while i < len(lav_app_date):
          test = []
          t1 = lav_app_date[i].split('/')[0]
          print(i)

          j = i
          while j < len(lav_app_date) and lav_app_date[j].split('/')[0] == t1:
              test.append(lav_app_date[j].split('/')[1])
              j += 1

          newdate = {
              'Day': t1,
              'time_sort': test
          }
          test1.append(newdate)

          i = j

      print(test1)
      return Response(test1)

                  
    except Exception as e:
            print(e)         

@api_view(['POST'])
def creategetappiontmenyclinicapi(request):
    try:
        data=request.data
        data['patient']=request.user.id
        ser=appcliSerSreializes(data=data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response({
                'status' : 400,
                'message' : 'something went wrong',
                'data':ser.errors

            })
    except Exception as e:
            print(e)  


@api_view(['GET'])
def getdoctoridapi(request,idDoc):
    
    ser = Doctor.objects.get(id=idDoc)

    serializer = doctorSerSreializes1(ser, many=False, context={'request': request})
    return Response(serializer.data)      

@api_view(['GET'])
def getclinidapi(request,idcli):
    
    ser = Clinic.objects.get(id=idcli)

    serializer = seviceSreializesapi(ser, many=False, context={'request': request})
    return Response(serializer.data)      
@api_view(['GET'])
def getthiidapi(request,idthi):
    
    ser = Therapist.objects.get(id=idthi)

    serializer = TherapistSreializes1(ser, many=False, context={'request': request})
    return Response(serializer.data)      

@api_view(['POST'])
def updateappiontmenycliniapi(request):
    try:
        data=request.data
        idoldapp=data['idoldapp']
        oldapp=Appointmentclinic.objects.get(id=idoldapp)
        oldapp.time=data['time']
        oldapp.Date=data['date']
        oldapp.save()
        return Response({
                'status' : 200,
                'message' : 'ubdate'

            })
    except Exception as e:
            print(e)   
@api_view(['POST'])
def updateappiontmenydoapi(request):
    try:
        data=request.data
        idoldapp=data['idoldapp']
        oldapp=AppointmentDoctor.objects.get(id=idoldapp)
        oldapp.time=data['time']
        oldapp.Date=data['date']
        oldapp.save()
        return Response({
                'status' : 200,
                'message' : 'ubdate'

            })

    except Exception as e:
            print(e)   


                  
     


@api_view(['POST'])
def createappiontmenydocapi(request):
    try:
        data=request.data
        data['patient']=request.user.id
        ser=appdocSerSreializes(data=data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response({
                'status' : 400,
                'message' : 'something went wrong',
                'data':ser.errors

            })
    except Exception as e:
            print(e)    

@api_view(['POST'])
def creatlikenews(request):
    try:
        data=request.data
        data['patient']=request.user.id
        ser=likenewsSerSreializes(data=data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response({
                'status' : 400,
                'message' : 'something went wrong',
                'data':ser.errors

            })
    except Exception as e:
            print(e)               
@api_view(['POST'])
def creatfavordoctor(request):
    try:
        data=request.data
        data['patient']=request.user.id
        ser=FaDoSerSreializes(data=data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response({
                'status' : 400,
                'message' : 'something went wrong',
                'data':ser.errors

            })
    except Exception as e:
            print(e) 

@api_view(['POST'])
def creatfavorclin(request):
    try:
        data=request.data
        data['patient']=request.user.id
        ser=FaCliSerSreializes(data=data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response({
                'status' : 400,
                'message' : 'something went wrong',
                'data':ser.errors

            })
    except Exception as e:
            print(e) 

@api_view(['POST'])
def creatfavorther(request):
    try:
        data=request.data
        data['patient']=request.user.id
        ser=FaTheSerSreializes(data=data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response({
                'status' : 400,
                'message' : 'something went wrong',
                'data':ser.errors

            })
    except Exception as e:
            print(e)  

@api_view(['POST'])
def creatCommentClir(request):
    try:
        data=request.data
        data['patient']=request.user.id
        ser=CoCliSerSreializes(data=data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response({
                'status' : 400,
                'message' : 'something went wrong',
                'data':ser.errors

            })
    except Exception as e:
            print(e)  


@api_view(['POST'])
def creatRatingCli(request):
    try:
        data=request.data
        data['patient']=request.user.id
        ser=RaCliSerSreializes(data=data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response({
                'status' : 400,
                'message' : 'something went wrong',
                'data':ser.errors

            })
    except Exception as e:
            print(e)        

# ------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------
def getDoctor(request):
    doctor1=Doctor.objects.all()
    sections=Section.objects.all()
    clin=Clinic.objects.all()


    return render(request ,'Doctor.html',{'var':'Doctors','doctors':doctor1,'sections':sections,'clinics':clin})

def getDoctorSection(request,pk):
    clin=Clinic.objects.all()
    sec=Section.objects.get(id=pk)
    doc=Doctor.objects.filter(section=sec).all()
    sections=Section.objects.all()
    return render(request ,'Doctor.html',{'var':'Doctors','doctors':doc,'sections':sections,'active_section': pk,'clinics':clin})


def creatDoctor(request):
    doctor1=Doctor.objects.all()
    sections=Section.objects.all()
    clin=Clinic.objects.all()
    if request.method=="POST":
       Name=request.POST['Name']
       price1=request.POST['price']
       specialization=request.POST['specialization']
       
       Description=request.POST['Description']
       secation1=request.POST['secation']
       im=request.FILES.get('Img')
       print(im)
       sec=Section.objects.get(id=secation1)
       Doctor.objects.create(price=price1,name=Name,specialization=specialization,Des=Description,section=sec,Img1=im)
       return redirect('centerapp:getDoctor')
    return render(request ,'Doctor.html',{'var':'Doctors','doctors':doctor1,'sections':sections,'clinics':clin})

def editDoctor(request):
    doctor1=Doctor.objects.all()
    sections=Section.objects.all()
    clin=Clinic.objects.all()

    if request.method=="POST":
       Name=request.POST['Name']
       specialization=request.POST['specialization']
       idd='o'
       Description=request.POST['Description']
       secation1=request.POST['secation']
       im=request.FILES.get('Img')

       iddoctor = request.POST['iddoctor']
       print(iddoctor)
       doc=Doctor.objects.get(id=iddoctor)
       print(doc)
       if Name:
           doc.name=Name
       if specialization:
           doc.specialization=specialization
       if Description :
           doc.Des=Description
       if secation1 :
           sec=Section.objects.get(id=secation1)
           doc.section=sec
       if im :
           doc.Img1=im                
       doc.save()  
           

       return redirect('centerapp:getDoctor')
    return render(request ,'Doctor.html',{'var':'Doctors','doctors':doctor1,'sections':sections,'clinics':clin})
  


def getthis(request):
    this1=Therapist.objects.all()
    clin=Clinic.objects.all()
    sections=Section.objects.all()



    return render(request ,'therapist.html',{'var':'Therapist','therapist':this1,'clinics':clin,'sections':sections})
 
def getthis1(request,idth):
    this1=Therapist.objects.all()
    clin=Clinic.objects.all()
    sections=Section.objects.all()
    thi=Therapist.objects.get(id=idth)
    if request.method=="POST":
    
       Name=request.POST['Name']
       specialization=request.POST['specialization']
       idd='o'
       Description=request.POST['Description']
       secation1=request.POST['secation']
       im=request.FILES.get('Img')


       th=Therapist.objects.get(id=idth)
       th.name=Name
       th.Des=Description
       cl=Clinic.objects.get(id=secation1)
       th.service=cl
       if im:
        th.Img1=im
       th.specialization=specialization
       th.save()
       return redirect('centerapp:getthis')
 





    return render(request ,'therapist1.html',{'var':'Therapist','therapist':this1,'thi':thi,'clinics':clin,'sections':sections})

def getthisClin(request,pk):
    clin=Clinic.objects.get(id=pk)
    this1=Therapist.objects.filter(service=clin).all()
    sections=Section.objects.all()
    clin1=Clinic.objects.all()
    return render(request,'therapist.html',{'var':'Therapist','therapist':this1,'clinics':clin1,'sections':sections})


def creattherapist(request):
    this1=Therapist.objects.all()
    clin1=Clinic.objects.all()
    sections=Section.objects.all()
    if request.method=="POST":
       Name=request.POST['name']
       specialization=request.POST['specialization']
       
       Description=request.POST['Des']
       service=request.POST['service']
       im=request.FILES.get('Img')
       print(im)
       clin=Clinic.objects.get(id=service)
       Therapist.objects.create(name=Name,specialization=specialization,Des=Description,service=clin,Img1=im)
       return redirect('centerapp:getthis')


    return render(request ,'therapist.html',{'var':'Therapist','therapist':this1,'clinics':clin1,'sections':sections})

def deletethi(request):
    if request.method=="POST":
        idth=request.POST['iddoctor']
        th=Therapist.objects.get(id=idth)
        th.delete()
        return redirect('centerapp:getthis')


    return render('centerapp:getthis')

def getDiv(request):
    Div=Device.objects.all()
    clin=Clinic.objects.all()
    sections=Section.objects.all()

    return render(request ,'Device.html',{'var':'Device','Devices':Div,'clinics':clin,'sections':sections})

def getDivClin(request,pk):
    clin=Clinic.objects.get(id=pk)
    Div=Device.objects.filter(service=clin).all()
    clin1=Clinic.objects.all()
    sections=Section.objects.all()
    return render(request ,'Device.html',{'var':'Device','Devices':Div,'clinics':clin1,'active_section': pk,'sections':sections})

def creatDevice(request):
    this1=Therapist.objects.all()
    clin1=Clinic.objects.all()
    sections=Section.objects.all()
    if request.method=="POST":
       Name=request.POST['name']

       price1=request.POST['price']
       Description=request.POST['Des']
       service=request.POST['service']
       im=request.FILES.get('Img')
       print(im)
       clin=Clinic.objects.get(id=service)
       Device.objects.create(price=price1,name=Name,Des=Description,service=clin,Img1=im)
       return redirect('centerapp:getDiv')


    return render(request ,'therapist.html',{'var':'Device','therapist':this1,'clinics':clin1,'sections':sections})

def deleteDevice(request):
    if request.method=="POST":
        idDe=request.POST['iddoctor']
        De=Device.objects.get(id=idDe)
        De.delete()
        return redirect('centerapp:getDiv')


    return render('centerapp:getthis')

def getDev1(request,idDev):
    this1=Therapist.objects.all()
    clin=Clinic.objects.all()
    sections=Section.objects.all()
    Dev=Device.objects.get(id=idDev)
    if request.method=="POST":
    
       Name=request.POST['Name']
       price1=request.POST['price']

       Description=request.POST['Description']
       secation1=request.POST['service']
       im=request.FILES.get('Img')
       Dev=Device.objects.get(id=idDev)
       Dev.name=Name
       Dev.price=price1
       Dev.Des=Description
       cl=Clinic.objects.get(id=secation1)
       Dev.service=cl
       if im:
        Dev.Img1=im

       Dev.save()
       return redirect('centerapp:getDiv')

    return render(request ,'Device1.html',{'var':'Device','therapist':this1,'Dev':Dev,'clinics':clin,'sections':sections})



def getNews(request):
    sections=Section.objects.all()
    clin=Clinic.objects.all()
    news=News.objects.all()
    return render(request ,'News.html',{'var':'news','news':news,'sections':sections,'clinics':clin})

def deleteNews(request):

    if request.method=="POST":

        idNews=request.POST['iddoctor']
        Ne=News.objects.get(id=idNews)
        Ne.delete()
        return redirect('centerapp:getNews')
    return render('centerapp:getNews')
 
def createNews(request):
    this1=Therapist.objects.all()
    clin1=Clinic.objects.all()
    sections=Section.objects.all()
    if request.method=="POST":
       Name=request.POST['name']
       

       
       Description=request.POST['Des']

       im=request.FILES.get('Img')

       News.objects.create(name=Name,Des=Description,Img1=im,date=datetime.now())
       return redirect('centerapp:getNews')


    return render(request ,'therapist.html',{'var':'news','therapist':this1,'clinics':clin1,'sections':sections})

def getNews1(request,idnew):
    sections=Section.objects.all()
    clin=Clinic.objects.all()

    news1=News.objects.get(id=idnew)
    if request.method=="POST":
    
       Name=request.POST['Name']
    #    Date1=request.POST['Date']

       Description=request.POST['Description']

       im=request.FILES.get('Img')
       news1=News.objects.get(id=idnew)
       news1.name=Name
       news1.Des=Description
    #    news1.date=Date1

       if im:
        news1.Img1=im

       news1.save()
       return redirect('centerapp:getNews')
    return render(request ,'News1.html',{'var':'news','news':news1,'sections':sections,'clinics':clin})


def getsection(request):
    sections=Section.objects.all()
    clin=Clinic.objects.all()
    return render(request ,'Sections.html',{'var':'Sections','sections':sections,'clinics':clin})

def getsection1(request,idsec):
    sections=Section.objects.all()
    clin=Clinic.objects.all()
    sec=Section.objects.get(id=idsec)
    if request.method=="POST":
       Name=request.POST['Name']

       fullname=request.POST['fullname']

       im=request.FILES.get('Img')
       sec=Section.objects.get(id=idsec)
       sec.name=Name
       sec.fullname=fullname

       if im:
        sec.Img1=im

       sec.save()
       return redirect('centerapp:getsection')

    return render(request ,'Section1.html',{'var':'Sections','sections':sections,'sec':sec,'clinics':clin})

def deletesection(request):
    sections=Section.objects.all()
    clin=Clinic.objects.all()

    if request.method=="POST":
        idSec=request.POST['iddoctor']
        sec=Section.objects.get(id=idSec)
        sec.delete()

        return redirect('centerapp:getsection')

    return render(request ,'Sections.html',{'var':'Sections','sections':sections,'clinics':clin})   

def createSection(request):
    sections=Section.objects.all()
    clin=Clinic.objects.all()
    if request.method=="POST":
       Name=request.POST['name']

       
       fullname=request.POST['fullname']

       im=request.FILES.get('Img')

       Section.objects.create(name=Name,fullname=fullname,Img1=im)
       return redirect('centerapp:getsection')


    return render(request ,'Sections.html',{'var':'Sections','sections':sections,'clinics':clin})   



def getclinic(request):
    sections=Section.objects.all()
    clin=Clinic.objects.all()
    return render(request ,'clinic.html',{'var':'clinices','sections':sections,'clinics':clin})

def getclinic1(request,idcli):
    sections=Section.objects.all()
    clin=Clinic.objects.all()
    cli=Clinic.objects.get(id=idcli)
    if request.method=="POST":
        Name=request.POST['Name']
        idRoomNumber=request.POST['idRoomNumber']
        floorNumber=request.POST['floorNumber']
        im=request.FILES.get('Img')
        if im:
            cli.Img1=im
        cli.name=Name
        cli.idRoomNumber=idRoomNumber
        cli.floorNumber=floorNumber
        cli.save() 
        return redirect('centerapp:getclinic')

    return render(request ,'clinic1.html',{'var':'clinices','cli':cli,'sections':sections,'clinics':clin})

def deleteclin(request):
    sections=Section.objects.all()
    clin=Clinic.objects.all()

    if request.method=="POST":
        idClin=request.POST['iddoctor']
        cli=Clinic.objects.get(id=idClin)
        cli.delete()

        return redirect('centerapp:getclinic')

    return render(request ,'clinic.html',{'var':'clinices','sections':sections,'clinics':clin})       

def createclin(request):
    sections=Section.objects.all()
    clin=Clinic.objects.all()
    if request.method=="POST":
       Name=request.POST['name']
       im=request.FILES.get('Img')

       
       floorNumber1=request.POST['floorNumber']

       idRoomNumber1=request.POST['idRoomNumber']

       Clinic.objects.create(name=Name,idRoomNumber=idRoomNumber1,floorNumber=floorNumber1,Img1=im)
       return redirect('centerapp:getclinic')


    return render(request ,'clinic.html',{'var':'clinices','sections':sections,'clinics':clin})   

def getpatient(request):
    sections=Section.objects.all()
    clin=Clinic.objects.all()
    pa=User.objects.filter(type='Patient')
    return render(request ,'patient.html',{'var':'patient','patient':pa,'sections':sections,'clinics':clin})

def getpatient1(request,idpa):
    sections=Section.objects.all()
    clin=Clinic.objects.all()
    pat=User.objects.get(id=idpa)
    if request.method=="POST":
        gender=request.POST['gender']
        birthday=request.POST['birthday']
        address=request.POST['address']
        photo=request.FILES.get('photo')
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']   
        print(birthday) 
                         
        pat.name=name
        pat.gender=gender
        pat.birthday=birthday

        pat.address=address
        pat.phone=phone
        pat.email=email
        if photo:
            pat.photo=photo

        pat.save() 
        return redirect('centerapp:getpatient')

    return render(request ,'patient1.html',{'var':'patient','pat':pat,'sections':sections,'clinics':clin})


def deletepatient(request):
    sections=Section.objects.all()
    clin=Clinic.objects.all()
    pa=User.objects.filter(type='Patient')
    if request.method=="POST":
        idpa=request.POST['iddoctor']
        pa=User.objects.get(id=idpa)
        pa.delete()

        return redirect('centerapp:getpatient')
    return render(request ,'patient.html',{'var':'patient','patient':pa,'sections':sections,'clinics':clin})

def createpatient(request):
    sections=Section.objects.all()
    clin=Clinic.objects.all()
    pa=User.objects.filter(type='Patient')
    if request.method=="POST":
        gender=request.POST['gender']
        birthday=request.POST['birthday']
        address=request.POST['address']
        photo=request.FILES.get('photo')
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']                               

        birthdaydatetime = datetime.strptime(birthday, '%Y-%m-%d').date()

        User.objects.create(name=name,gender=gender,birthday=birthdaydatetime,address=address,phone=phone,email=email,photo=photo,type='Patient')
        return redirect('centerapp:getpatient')

    return render(request ,'patient.html',{'var':'patient','patient':pa,'sections':sections,'clinics':clin})

def getdaywork(request):
    sections=Section.objects.all()
    clin=Clinic.objects.all()
    daywork=Daywork.objects.all()
    Doctors=Employ.objects.all()
    for i in daywork:
        if i.code==0:
            i.name="Monday"
        if i.code==1:
            i.name="Tuesday"
        if i.code==2:
            i.name="Wednesday"
        if i.code==3:
            i.name="Thursday"
        if i.code==4:
            i.name="Friday"            
        if i.code==5:
            i.name="Saturday"
        if i.code==6:
            i.name="Sunday"            
    return render(request ,'Daywork.html',{'var':'workday','daywork':daywork,'Doctors':Doctors,'sections':sections,'clinics':clin})
def getDaywork1(request,idDay):
    sections=Section.objects.all()
    clin=Clinic.objects.all()
    Day=Daywork.objects.get(id=idDay)
    emp=Employ.objects.all()
    if request.method=="POST":
        Name=request.POST['name']
        startwork1=request.POST['startwork']
        endwork1=request.POST['endwork']
        em=request.POST['Doctor']
        day=Daywork.objects.get(id=idDay)
        if Name:
         day.code=Name
        if startwork1:
            day.startwork=startwork1
        if endwork1:    
           day.endwork=endwork1
        e=Employ.objects.get(id=em)   
        day.Employ=e
        day.save() 
        return redirect('centerapp:getdaywork')

    return render(request ,'Daywork1.html',{'var':'workday','day':Day,'sections':sections,'clinics':clin,'Employ':emp})

def getpatient1(request,idpa):
    sections=Section.objects.all()
    clin=Clinic.objects.all()
    pat=User.objects.get(id=idpa)
    if request.method=="POST":
        gender=request.POST['gender']
        birthday=request.POST['birthday']
        address=request.POST['address']
        photo=request.FILES.get('photo')
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']   
        print(birthday) 
                         
        pat.name=name
        pat.gender=gender
        pat.birthday=birthday

        pat.address=address
        pat.phone=phone
        pat.email=email
        if photo:
            pat.photo=photo

        pat.save() 
        return redirect('centerapp:getpatient')

    return render(request ,'patient1.html',{'var':'patient','pat':pat,'sections':sections,'clinics':clin})


def deleteDaywork(request):
    sections=Section.objects.all()
    clin=Clinic.objects.all()
    daywork=Daywork.objects.all()
    for i in daywork:
        if i.code==0:
            i.name="Monday"
        if i.code==1:
            i.name="Tuesday"
        if i.code==2:
            i.name="Wednesday"
        if i.code==3:
            i.name="Thursday"
        if i.code==4:
            i.name="Friday"            
        if i.code==5:
            i.name="Saturday"
        if i.code==6:
            i.name="Sunday"  
    if request.method=="POST":
        idDay=request.POST['iddoctor']
        Da=Daywork.objects.get(id=idDay)
        Da.delete()

        return redirect('centerapp:getdaywork')
    return render('centerapp:getdaywork')

def createDaywork(request):
    sections=Section.objects.all()
    clin=Clinic.objects.all()
    daywork=Daywork.objects.all()
    for i in daywork:
        if i.code==0:
            i.name="Monday"
        if i.code==1:
            i.name="Tuesday"
        if i.code==2:
            i.name="Wednesday"
        if i.code==3:
            i.name="Thursday"
        if i.code==4:
            i.name="Friday"            
        if i.code==5:
            i.name="Saturday"
        if i.code==6:
            i.name="Sunday"  
    if request.method=="POST":
        endwork2=request.POST['endwork']
        startwork2=request.POST['startwork']
        Doctor1=request.POST['Doctor']
        name=request.POST['name']
        do=Employ.objects.get(id=Doctor1)
        if name=="Monday":
            code1=0
        if name=="Tuesday":
            code1=1
        if name=="Wednesday":
            code1=2
        if name=="Thursday":
            code1=3
        if name=="Friday":
            code1=4            
        if name=="Saturday":
            code1=5
        if name=="Sunday":
            code1=6  

                

        Daywork.objects.create(code=code1,startwork=startwork2,endwork=endwork2,Employ=do)
        return redirect('centerapp:getdaywork')
    return render(request ,'Daywork.html',{'var':'workday','daywork':daywork,'sections':sections,'clinics':clin})


def getstaiteces(request):
    sections=Section.objects.all()
    clin=Clinic.objects.all()
    if request.method=="POST":
        idtype=request.POST['idtype']
        idsec=request.POST['idsec']
        idcli=request.POST['idcli']
        if idcli !='0':
         cli=Clinic.objects.get(id=idcli)
         does=Therapist.objects.filter(service=cli)
         do=[]
         appcont=[]
         for i in does:
            nDate=datetime.now().date()
            if idtype=="Monthy":
              dat=nDate-timedelta(days=30)
            if idtype=="Weekly":
              dat=nDate-timedelta(days=7)
            do.append(i.name)
            app=Appointmentclinic.objects.filter(
    Q(therapist=i) &
    Q(Date__gt=dat)
).count()
            
            appcont.append(app)
         print(appcont)
         print(do)    
        if idsec !='0':
         sec=Section.objects.get(id=idsec)
         does=Doctor.objects.filter(section=sec)
         do=[]
         appcont=[]
         for i in does:
            nDate=datetime.now().date()
            if idtype=="Monthy":
              dat=nDate-timedelta(days=30)
            if idtype=="Weekly":
              dat=nDate-timedelta(days=7)
            do.append(i.name)
            app=AppointmentDoctor.objects.filter(
    Q(doctor=i) &
    Q(Date__gt=dat)
).count()
            
            appcont.append(app)
         print(appcont)
         print(do)    
        return render(request ,'Staiteces.html',{'var':'Staiteces','does':do,'appcont':appcont,'sections':sections,'clinics':clin})  

    return render(request ,'Staiteces.html',{'var':'Staiteces','sections':sections,'clinics':clin})

def getappintmentdoctor(request):
    sections=Section.objects.all()
    clin=Clinic.objects.all()
    apps=AppointmentDoctor.objects.all().order_by('Date')
    print(apps)
    return render(request ,'appointment.html',{'var':'Appointments','apps':apps,'sections':sections,'clinics':clin})



def showappointment(request):
    doctor1 = Doctor.objects.all()
    sections = Section.objects.all()
    clin = Clinic.objects.all()
    av_app_date = []
    lav_app_date = []
    if request.method=="POST":
     idDoc = request.POST['idDoc']
     doctor1=Doctor.objects.get(id=idDoc)
     gmailuser=request.POST['pgmail']
     user=User.objects.get(email=gmailuser)
     if user:
      print(idDoc)
      current_date = datetime.now().date()

      day = Daywork.objects.filter(Employ=idDoc).all()
      for l in range(4):
       for i in day:
        if i.code==0:
            dayname="Monday"
        if i.code==1:
            dayname="Tuesday"
        if i.code==2:
            dayname="Wednesday"
        if i.code==3:
            dayname="Thursday"
        if i.code==4:
            dayname="Friday"
        if i.code==5:
            dayname="Saturday"
        if i.code==6:
            dayname="Sunday"                                                                        
        next_day = current_date + timedelta(days=((i.code - current_date.weekday()) % 7)+7*l)

        appointments = AppointmentDoctor.objects.filter(doctor=idDoc, Date=next_day).order_by('time')


        
        start_datetime = datetime.combine(next_day, i.startwork)
        final_datetime = datetime.combine(next_day, i.endwork)        
        finalapppiont = datetime.combine(next_day, time(hour=0, minute=0, second=0))
        finalapppiont1 = datetime.combine(next_day, time(hour=0, minute=0, second=0))
        if appointments:
          for j in appointments:
            finalapppiont=datetime.combine(next_day, j.time)

            j_datetime = datetime.combine(next_day, j.time)  
            print(start_datetime)
            print(j_datetime)
            if j_datetime >= start_datetime + timedelta(minutes=30):
                print('i')
                
                y = f"{dayname},{next_day.strftime('%Y-%m-%d')}/{start_datetime.strftime('%H:%M:%S')},{j_datetime.strftime('%H:%M:%S')}"
                av_app_date.append(y)
                start_datetime = j_datetime + timedelta(minutes=30) 
            else:
                start_datetime = start_datetime+ timedelta(minutes=30) 

          y = f"{dayname},{next_day.strftime('%Y-%m-%d')}/{(finalapppiont+ timedelta(minutes=30)).strftime('%H:%M:%S')},{final_datetime.strftime('%H:%M:%S')}"
          av_app_date.append(y)
        else:
              y = f"{dayname},{next_day.strftime('%Y-%m-%d')}/{i.startwork.strftime('%H:%M:%S')},{i.endwork.strftime('%H:%M:%S')}"
              av_app_date.append(y)   
      print(av_app_date)                    
      for k in av_app_date:
            p1,p2=k.split('/')
          

            dname,date_str= p1.split(',')
            start_time_str, end_time_str = p2.split(',')            

            date = datetime.strptime(date_str, '%Y-%m-%d').date()
            start_datetime = datetime.strptime(start_time_str, '%H:%M:%S')
            end_datetime = datetime.strptime(end_time_str, '%H:%M:%S')

            while end_datetime >= start_datetime + timedelta(minutes=30):
                y = f"{dname},{date.strftime('%Y-%m-%d')}/{start_datetime.strftime('%H:%M:%S')},{(start_datetime + timedelta(minutes=30)).strftime('%H:%M:%S')}"
                print(y)
                lav_app_date.append(y)
                start_datetime = start_datetime + timedelta(minutes=30) 
                
      test1 = []  # Initialize the outer list
      i = 0  # Initialize the outer loop index

      while i < len(lav_app_date):
          test = []
          t1 = lav_app_date[i].split('/')[0]
          print(i)

          j = i
          while j < len(lav_app_date) and lav_app_date[j].split('/')[0] == t1:
              test.append(lav_app_date[j].split('/')[1])
              j += 1

          newdate = {
              'Day': t1,
              'time_sort': test
          }
          test1.append(newdate)

          i = j

      print(test1)

      return render(request, 'createappointment2.html', {'var': 'Appointments', 'doctor':doctor1,'user':user ,'av_app_date':test1, 'sections': sections, 'clinics': clin})
    
    

    return render(request, 'createappointment.html', {'var': 'Appointments', 'doctors': doctor1,'av_app_date':lav_app_date, 'sections': sections, 'clinics': clin})
def createappointment(request):
    doctor1 = Doctor.objects.all()
    sections = Section.objects.all()
    clin = Clinic.objects.all()
    if request.method=="POST":
        iduser=request.POST['pgmail']
        
        idoc=request.POST['doctoe']
        D=request.POST['Date']
        T=request.POST['time']
        print(D)
        print(T)
        # print(iduser)
        # print(idoc)
        # print(appiontment)
        # dname,date_str, start_time_str, end_time_str = appiontment.split(',')

        # date = datetime.strptime(date_str, '%Y-%m-%d').date()
        # start_datetime = datetime.strptime(start_time_str, '%H:%M:%S')
        Do1=Doctor.objects.get(id=idoc)
        pa1=User.objects.get(id=iduser)
        AppointmentDoctor.objects.create(doctor=Do1,patient=pa1,Date=D,time=T) 
        return redirect('centerapp:getappintmentdoctor')      
   

    return render(request, 'appointment.html', {'var': 'Appointments', 'doctors': doctor1, 'sections': sections, 'clinics': clin})

def createappointmentcli(request):
    doctor1 = Doctor.objects.all()
    sections = Section.objects.all()
    clin = Clinic.objects.all()
    if request.method=="POST":
        iduser=request.POST['pgmail']
        
        idoc=request.POST['idDoc']
        de=request.POST['idDev']
        D=request.POST['Date']
        T=request.POST['time'].split(',')[0]
        print(D)
        print(T)
        # print(iduser)
        # print(idoc)
        # print(appiontment)
        # dname,date_str, start_time_str, end_time_str = appiontment.split(',')

        # date = datetime.strptime(date_str, '%Y-%m-%d').date()
        # start_datetime = datetime.strptime(start_time_str, '%H:%M:%S')
        Date1=D.split(',')[1]
        Do1=Therapist.objects.get(id=idoc)
        Dev=Device.objects.get(id=de)
        pa1=User.objects.get(id=iduser)
        Appointmentclinic.objects.create(therapist=Do1,patient=pa1,Date=Date1,time=T,device=Dev) 
        return redirect('centerapp:getappintmentclinice')      
   

    return render(request, 'appointment.html', {'var': 'clAppointments', 'doctors': doctor1, 'sections': sections, 'clinics': clin})


def deleteappiontmentdoctor(request):
    sections=Section.objects.all()
    clin=Clinic.objects.all()
    apps=AppointmentDoctor.objects.all().order_by('Date')
    if request.method=="POST":

         idapp = request.POST['iddoctor']  
         app=AppointmentDoctor.objects.get(id=idapp)    
         app.delete()
         return redirect('centerapp:getappintmentdoctor')

    return render(request ,'appointment.html',{'var':'Appointments','apps':apps,'sections':sections,'clinics':clin})


def getappintmentclinice(request):
    sections=Section.objects.all()
    clin=Clinic.objects.all()
    apps=Appointmentclinic.objects.all().order_by('Date')
    print(apps)
    return render(request ,'appointmentclin.html',{'var':'cliAppointments','apps':apps,'sections':sections,'clinics':clin})



def showappointmentcli(request):
    the = Therapist.objects.all()
    sections = Section.objects.all()
    clin = Clinic.objects.all()
    Device1=Device.objects.all()
    av_app_date = []
    lav_app_date = []
    if request.method=="POST":
     idDoc = request.POST['idDoc']
     idDev = request.POST['idDev']
     the=Therapist.objects.get(id=idDoc)
     Dev=Device.objects.get(id=idDev)
     gmailuser=request.POST['pgmail']
     user=User.objects.get(email=gmailuser)
     if user:
      appointments=[]
      print(idDoc)
      current_date = datetime.now().date()

      day = Daywork.objects.filter(Employ=idDoc).all()
      for l in range(4):
       for i in day:
        if i.code==0:
            dayname="Monday"
        if i.code==1:
            dayname="Tuesday"
        if i.code==2:
            dayname="Wednesday"
        if i.code==3:
            dayname="Thursday"
        if i.code==4:
            dayname="Friday"
        if i.code==5:
            dayname="Saturday"
        if i.code==6:
            dayname="Sunday"                                                                        
        next_day = current_date + timedelta(days=((i.code - current_date.weekday()) % 7)+7*l)

        appointments = Appointmentclinic.objects.filter(therapist=idDoc, Date=next_day).order_by('time')
       
        
        start_datetime = datetime.combine(next_day, i.startwork)
        final_datetime = datetime.combine(next_day, i.endwork)        
        finalapppiont = datetime.combine(next_day, time(hour=0, minute=0, second=0))
        finalapppiont1 = datetime.combine(next_day, time(hour=0, minute=0, second=0))
        if appointments:
          for j in appointments:
            finalapppiont=datetime.combine(next_day, j.time)

            j_datetime = datetime.combine(next_day, j.time)  
            print(start_datetime)
            print(j_datetime)
            if j_datetime >= start_datetime + timedelta(minutes=30):
                print('i')
                
                y = f"{dayname},{next_day.strftime('%Y-%m-%d')}/{start_datetime.strftime('%H:%M:%S')},{j_datetime.strftime('%H:%M:%S')}"
                av_app_date.append(y)
                start_datetime = j_datetime + timedelta(minutes=30) 
            else:
                start_datetime = start_datetime+ timedelta(minutes=30) 

          y = f"{dayname},{next_day.strftime('%Y-%m-%d')}/{(finalapppiont+ timedelta(minutes=30)).strftime('%H:%M:%S')},{final_datetime.strftime('%H:%M:%S')}"
          av_app_date.append(y)
        else:
              y = f"{dayname},{next_day.strftime('%Y-%m-%d')}/{i.startwork.strftime('%H:%M:%S')},{i.endwork.strftime('%H:%M:%S')}"
              av_app_date.append(y)   
      print(av_app_date)                    
      for k in av_app_date:
            p1,p2=k.split('/')
          

            dname,date_str= p1.split(',')
            start_time_str, end_time_str = p2.split(',')            

            date = datetime.strptime(date_str, '%Y-%m-%d').date()
            start_datetime = datetime.strptime(start_time_str, '%H:%M:%S')
            end_datetime = datetime.strptime(end_time_str, '%H:%M:%S')
            appointments2 = Appointmentclinic.objects.filter(device=idDev, Date=date).order_by('time')
            
            while end_datetime >= start_datetime + timedelta(minutes=30):
                t=None
                t=appointments2.filter(time=start_datetime).first()
                if t==None:

                  y = f"{dname},{date.strftime('%Y-%m-%d')}/{start_datetime.strftime('%H:%M:%S')},{(start_datetime + timedelta(minutes=30)).strftime('%H:%M:%S')}"
                  print(y)
                  lav_app_date.append(y)
                start_datetime = start_datetime + timedelta(minutes=30) 
                
      test1 = []  # Initialize the outer list
      i = 0  # Initialize the outer loop index

      while i < len(lav_app_date):
          test = []
          t1 = lav_app_date[i].split('/')[0]
          print(i)

          j = i
          while j < len(lav_app_date) and lav_app_date[j].split('/')[0] == t1:
              test.append(lav_app_date[j].split('/')[1])
              j += 1

          newdate = {
              'Day': t1,
              'time_sort': test
          }
          test1.append(newdate)

          i = j

      print(test1)

      return render(request, 'createappointmentclin2.html', {'var': 'Appointmentsclin','Device':Dev, 'Therapist':the,'user':user ,'av_app_date':test1, 'sections': sections, 'clinics': clin})
    
    

    return render(request, 'createappointmentcli.html', {'var': 'Appointmentsclin', 'Therapist':the,'av_app_date':lav_app_date,'Device':Device1, 'sections': sections, 'clinics': clin})




def deletedoctoer(request):
    doctor1=Doctor.objects.all()
    sections=Section.objects.all()
    clin=Clinic.objects.all()
    if request.method=="POST":

         iddoctor = request.POST['iddoctor']  
         print(iddoctor) 
         doc=Doctor.objects.get(id=iddoctor)    
         doc.delete()
         return redirect('centerapp:getDoctor')
    return render(request ,'Doctor.html',{'var':'Doctors','doctors':doctor1,'sections':sections,'clinics':clin})






@login_required
def home(request):
    # Redirect the user based on their user type
    if request.user.type == 'Manager':
        return redirect('centerapp:getDoctor')
    elif request.user.type == 'Recption':
        return redirect('centerapp:Rgetpatient')
    else:
        return redirect('urlDefault')  # Redirect to a default URL for other user types

def login1(request):
    if request.method == 'POST':
        username = request.POST['Name']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            print("ok")
            return redirect('centerapp:home')  # Redirect to the home view after successful login
        else:
            # Handle invalid login credentials
            print("nook")
            return render(request, 'login.html', {'error_message': 'Invalid login credentials'})
    else:
        return render(request, 'login.html')



def getmap(request):
    return render(request,'map.html')

def getabout(request):
       
    sections=Section.objects.all()
    clin=Clinic.objects.all()
    about1=about.objects.all()
    return render(request ,'about.html',{'var':'about','about':about1,'sections':sections,'clinics':clin})

def Editabout(request,idab):
       
    sections=Section.objects.all()
    clin=Clinic.objects.all()

    abou=about.objects.get(id=idab)
    if request.method=="POST":
        abou=about.objects.get(id=idab)
        wa=request.POST['whatsapp']
        ins=request.POST['Instagram']
        yo=request.POST['Youtube']
        fa=request.POST['facebook']
        co=request.POST['country']
        la=request.POST['lat'] 
        lo=request.POST['long'] 
        abou.whatsapp=wa
        abou.Instagram=ins
        abou.youtube=yo
        abou.fasebook=fa
        abou.loction.country=co
        abou.loction.lat=la
        abou.loction.long=lo
        abou.loction.save()
        abou.save()
        return redirect('centerapp:getabout')

    return render(request ,'about1.html',{'var':'about','about':abou,'sections':sections,'clinics':clin})

def getchat(request):
    return render(request,'chat1.html')
# ---------------------------------------------------------------------------------------------------

def getoffer(request):
    sections=Section.objects.all()
    clin=Clinic.objects.all()
    offer1=offer.objects.all()
    does=Therapist.objects.all()
    
    return render(request ,'offer.html',{'var':'offer','offer':offer1,'doctors':does,'sections':sections,'clinics':clin})

def deleteoffer(request):

    if request.method=="POST":

        idoffer=request.POST['iddoctor']
        off=offer.objects.get(id=idoffer)
        off.delete()
        return redirect('centerapp:getoffer')
    return render('centerapp:getoffer')
 
def createoffer(request):

    if request.method=="POST":
       photo=request.FILES.get('Img')
       Name=request.POST['name']
       date1=request.POST['date']
       oldprice1=request.POST['oldprice']       
       discount1=request.POST['discount']
       doctor1=request.POST['doctor']
       durtion1=request.POST['durtion']
       cli=request.POST['clinice']
       cli1=Clinic.objects.get(id=cli)
       doc=Therapist.objects.get(id=doctor1)
                
       offer.objects.create(Img1=photo,name=Name,date=date1,oldprice=oldprice1,discount=discount1,durtion=durtion1,doctor=doc,sevice=cli1)
       return redirect('centerapp:getoffer')


    return render('centerapp:getoffer')

def showoffer(request,idoff):
    sections=Section.objects.all()
    clin=Clinic.objects.all()
    does=Therapist.objects.all()
    
    offer1=offer.objects.get(id=idoff)
    if request.method=="POST":
       photo=request.FILES.get('Img')     
       Name=request.POST['name']
       date1=request.POST['date']
       oldprice1=request.POST['oldprice']       
       discount1=request.POST['discount']
       doctor1=request.POST['doctor']
       durtion1=request.POST['durtion']
       cli=request.POST['clinice'] 
       print(cli)      
       doc=Therapist.objects.get(id=doctor1)
       cli12=Clinic.objects.get(id=cli)

       if photo:
           offer1.Img1=photo
       offer1.sevice=cli12
       offer1.name=Name
       offer1.date=date1
       offer1.durtion=durtion1
       offer1.discount=discount1
       offer1.oldprice=oldprice1
       offer1.doctor=doc

       offer1.save()
       return redirect('centerapp:getoffer')
    return render(request ,'offer1.html',{'var':'offer','doctors':does,'offer':offer1,'sections':sections,'clinics':clin})


def editeuser(request):
    sections=Section.objects.all()
    clin=Clinic.objects.all()
    apps=AppointmentDoctor.objects.all().order_by('Date')
    if request.method=="POST":

         phone1 = request.POST['phone']  
         address1 = request.POST['address']
         photo1 =request.FILES.get('photo')
         user1=request.user
         user1.phone=phone1
         user1.address=address1
         if photo1:
             user1.photo=photo1
         user1.save()
         return redirect('centerapp:getappintmentdoctor')

    return render(request ,'appointment.html',{'var':'Appointments','apps':apps,'sections':sections,'clinics':clin})

import json
from django.http.request import HttpHeaders
from django.shortcuts import render

from django.http import HttpResponse
import requests


def send_notification(registration_ids , message_title , message_desc):
    fcm_api = ""
    url = "https://fcm.googleapis.com/fcm/send"
    
    headers = {
    "Content-Type":"application/json",
    "Authorization": 'key='+fcm_api}

    payload = {
        "registration_ids" :registration_ids,
        "priority" : "high",
        "notification" : {
            "body" : message_desc,
            "title" : message_title,
            "image" : "https://i.ytimg.com/vi/m5WUPHRgdOA/hqdefault.jpg?sqp=-oaymwEXCOADEI4CSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLDwz-yjKEdwxvKjwMANGk5BedCOXQ",
            "icon": "https://yt3.ggpht.com/ytc/AKedOLSMvoy4DeAVkMSAuiuaBdIGKC7a5Ib75bKzKO3jHg=s900-c-k-c0x00ffffff-no-rj",
            
        }
    }

    result = requests.post(url,  data=json.dumps(payload), headers=headers )
    print(result.json())





def index(request):
    return render(request , 'index.html')

def send(request):
    resgistration  = [
    ]
    send_notification(resgistration , 'Code Keen added a new video' , 'Code Keen new video alert')
    return HttpResponse("sent")




def showFirebaseJS(request):
    data='importScripts("https://www.gstatic.com/firebasejs/8.2.0/firebase-app.js");' \
         'importScripts("https://www.gstatic.com/firebasejs/8.2.0/firebase-messaging.js"); ' \
         'var firebaseConfig = {' \
         '        apiKey: "",' \
         '        authDomain: "",' \
         '        databaseURL: "",' \
         '        projectId: "",' \
         '        storageBucket: "",' \
         '        messagingSenderId: "",' \
         '        appId: "",' \
         '        measurementId: ""' \
         ' };' \
         'firebase.initializeApp(firebaseConfig);' \
         'const messaging=firebase.messaging();' \
         'messaging.setBackgroundMessageHandler(function (payload) {' \
         '    console.log(payload);' \
         '    const notification=JSON.parse(payload);' \
         '    const notificationOption={' \
         '        body:notification.body,' \
         '        icon:notification.icon' \
         '    };' \
         '    return self.registration.showNotification(payload.notification.title,notificationOption);' \
         '});'

    return HttpResponse(data,content_type="text/javascript")

def notf(request):
    return render(request,'notif.html')

def getdoc1(request,iddoc):
    this1=Therapist.objects.all()
    clin=Clinic.objects.all()
    sections=Section.objects.all()
    doc=Doctor.objects.get(id=iddoc)
    if request.method=="POST":
    
       Name=request.POST['Name']
       price1=request.POST['price']
       specialization=request.POST['specialization']
   
       Description=request.POST['Description']
       secation1=request.POST['secation']
       im=request.FILES.get('Img')


       th=Doctor.objects.get(id=iddoc)
       th.name=Name
       th.Des=Description
       th.price=price1
       cl=Section.objects.get(id=secation1)
       th.section=cl
       if im:
        th.Img1=im
       th.specialization=specialization
       th.save()
       return redirect('centerapp:getDoctor')
    return render(request ,'doctor1.html',{'var':'Doctor','doc':doc,'clinics':clin,'sections':sections})
# ------------------------------------------------------------------------------------------------------------------
def getRec(request):
    sections=Section.objects.all()
    clin=Clinic.objects.all()
    recaptions=User.objects.filter(type="Recption")
    return render(request ,'Recaption.html',{'var':'recaption','rec':recaptions,'sections':sections,'clinics':clin})


def getRec1(request,idRe):
    sections=Section.objects.all()
    clin=Clinic.objects.all()

    re=User.objects.get(id=idRe)
    if request.method=="POST":
    
       address1=request.POST['address']
    #    Date1=request.POST['Date']

       phone1=request.POST['phone']

       im=request.FILES.get('Img')
       re=User.objects.get(id=idRe)
       re.address=address1
       re.phone=phone1
    #    news1.date=Date1

       if im:
        re.photo=im

       re.save()
       return redirect('centerapp:getRec')
    return render(request ,'Recaption1.html',{'var':'recaption','recaptions':re,'sections':sections,'clinics':clin})


def creatRecaptions(request):
    this1=Therapist.objects.all()
    clin1=Clinic.objects.all()
    sections=Section.objects.all()
    if request.method=="POST":
       Name=request.POST['name']
       em=request.POST['email']
       ge=request.POST['gender']
       br=request.POST['birthday']
       ad=request.POST['address']
       ph=request.POST['Phone']

       im=request.FILES.get('Img')
       

       User.objects.create(name=Name,type='Recption',photo=im,birthday=br,email=em,address=ad,phone=ph,gender=ge,username=Name)
       return redirect('centerapp:getRec')


    return render('centerapp:getRec')


def deleteRecaptions(request):

    if request.method=="POST":

        idre=request.POST['iddoctor']
        Ne=User.objects.get(id=idre)
        Ne.delete()
        return redirect('centerapp:getRec')
    return render('centerapp:getRec')
 
# -------------------------------------------------------------------------------------------
def Rgetappintmentclinice(request):
    sections=Section.objects.all()
    clin=Clinic.objects.all()
    apps=Appointmentclinic.objects.all().order_by('Date')
    print(apps)
    return render(request ,'Rappointmentclin.html',{'var':'clAppointments','apps':apps,'sections':sections,'clinics':clin})


def Rshowappointmentcli(request):
    the = Therapist.objects.all()
    sections = Section.objects.all()
    clin = Clinic.objects.all()
    Device1=Device.objects.all()
    av_app_date = []
    lav_app_date = []
    if request.method=="POST":
     idDoc = request.POST['idDoc']
     idDev = request.POST['idDev']
     the=Therapist.objects.get(id=idDoc)
     Dev=Device.objects.get(id=idDev)
     gmailuser=request.POST['pgmail']
     user=User.objects.get(email=gmailuser)
     if user:
      appointments=[]
      print(idDoc)
      current_date = datetime.now().date()

      day = Daywork.objects.filter(Employ=idDoc).all()
      for l in range(4):
       for i in day:
        if i.code==0:
            dayname="Monday"
        if i.code==1:
            dayname="Tuesday"
        if i.code==2:
            dayname="Wednesday"
        if i.code==3:
            dayname="Thursday"
        if i.code==4:
            dayname="Friday"
        if i.code==5:
            dayname="Saturday"
        if i.code==6:
            dayname="Sunday"                                                                        
        next_day = current_date + timedelta(days=((i.code - current_date.weekday()) % 7)+7*l)

        appointments = Appointmentclinic.objects.filter(therapist=idDoc, Date=next_day).order_by('time')
       
        
        start_datetime = datetime.combine(next_day, i.startwork)
        final_datetime = datetime.combine(next_day, i.endwork)        
        finalapppiont = datetime.combine(next_day, time(hour=0, minute=0, second=0))
        finalapppiont1 = datetime.combine(next_day, time(hour=0, minute=0, second=0))
        if appointments:
          for j in appointments:
            finalapppiont=datetime.combine(next_day, j.time)

            j_datetime = datetime.combine(next_day, j.time)  
            print(start_datetime)
            print(j_datetime)
            if j_datetime >= start_datetime + timedelta(minutes=30):
                print('i')
                
                y = f"{dayname},{next_day.strftime('%Y-%m-%d')}/{start_datetime.strftime('%H:%M:%S')},{j_datetime.strftime('%H:%M:%S')}"
                av_app_date.append(y)
                start_datetime = j_datetime + timedelta(minutes=30) 
            else:
                start_datetime = start_datetime+ timedelta(minutes=30) 

          y = f"{dayname},{next_day.strftime('%Y-%m-%d')}/{(finalapppiont+ timedelta(minutes=30)).strftime('%H:%M:%S')},{final_datetime.strftime('%H:%M:%S')}"
          av_app_date.append(y)
        else:
              y = f"{dayname},{next_day.strftime('%Y-%m-%d')}/{i.startwork.strftime('%H:%M:%S')},{i.endwork.strftime('%H:%M:%S')}"
              av_app_date.append(y)   
      print(av_app_date)                    
      for k in av_app_date:
            p1,p2=k.split('/')
          

            dname,date_str= p1.split(',')
            start_time_str, end_time_str = p2.split(',')            

            date = datetime.strptime(date_str, '%Y-%m-%d').date()
            start_datetime = datetime.strptime(start_time_str, '%H:%M:%S')
            end_datetime = datetime.strptime(end_time_str, '%H:%M:%S')
            appointments2 = Appointmentclinic.objects.filter(device=idDev, Date=date).order_by('time')
            
            while end_datetime >= start_datetime + timedelta(minutes=30):
                t=None
                t=appointments2.filter(time=start_datetime).first()
                if t==None:

                  y = f"{dname},{date.strftime('%Y-%m-%d')}/{start_datetime.strftime('%H:%M:%S')},{(start_datetime + timedelta(minutes=30)).strftime('%H:%M:%S')}"
                  print(y)
                  lav_app_date.append(y)
                start_datetime = start_datetime + timedelta(minutes=30) 
                
      test1 = []  # Initialize the outer list
      i = 0  # Initialize the outer loop index

      while i < len(lav_app_date):
          test = []
          t1 = lav_app_date[i].split('/')[0]
          print(i)

          j = i
          while j < len(lav_app_date) and lav_app_date[j].split('/')[0] == t1:
              test.append(lav_app_date[j].split('/')[1])
              j += 1

          newdate = {
              'Day': t1,
              'time_sort': test
          }
          test1.append(newdate)

          i = j

      print(test1)

      return render(request, 'Rcreateappointmentclin2.html', {'var': 'clAppointments','Device':Dev, 'Therapist':the,'user':user ,'av_app_date':test1, 'sections': sections, 'clinics': clin})
    
    

    return render(request, 'Rcreateappointmentcli.html', {'var': 'clAppointments', 'Therapist':the,'av_app_date':lav_app_date,'Device':Device1, 'sections': sections, 'clinics': clin})

def deleteappiontmentcli(request):
    sections=Section.objects.all()
    clin=Clinic.objects.all()
    apps=AppointmentDoctor.objects.all().order_by('Date')
    if request.method=="POST":

         idapp = request.POST['iddoctor']  
         app=Appointmentclinic.objects.get(id=idapp)    
         app.delete()
         return redirect('centerapp:getappintmentclinice')

    return render('centerapp:getappintmentclinice')


def Rdeleteappiontmentcli(request):
    sections=Section.objects.all()
    clin=Clinic.objects.all()
    apps=AppointmentDoctor.objects.all().order_by('Date')
    if request.method=="POST":

         idapp = request.POST['iddoctor']  
         app=Appointmentclinic.objects.get(id=idapp)    
         app.delete()
         return redirect('centerapp:Rgetappintmentclinice')

    return render('centerapp:Rgetappintmentclinice')
def Rdeleteappiontmentdoctor(request):
    sections=Section.objects.all()
    clin=Clinic.objects.all()
    apps=AppointmentDoctor.objects.all().order_by('Date')
    if request.method=="POST":

         idapp = request.POST['iddoctor']  
         app=AppointmentDoctor.objects.get(id=idapp)    
         app.delete()
         return redirect('centerapp:Rgetappintmentdoctor')

    return render('centerapp:Rgetappintmentdoctor')

def Rcreateappointmentcli(request):
    doctor1 = Doctor.objects.all()
    sections = Section.objects.all()
    clin = Clinic.objects.all()
    if request.method=="POST":
        iduser=request.POST['pgmail']
        
        idoc=request.POST['idDoc']
        de=request.POST['idDev']
        D=request.POST['Date']
        T=request.POST['time'].split(',')[0]
        print(D)
        print(T)
        # print(iduser)
        # print(idoc)
        # print(appiontment)
        # dname,date_str, start_time_str, end_time_str = appiontment.split(',')

        # date = datetime.strptime(date_str, '%Y-%m-%d').date()
        # start_datetime = datetime.strptime(start_time_str, '%H:%M:%S')
        Date1=D.split(',')[1]
        Do1=Therapist.objects.get(id=idoc)
        Dev=Device.objects.get(id=de)
        pa1=User.objects.get(id=iduser)
        Appointmentclinic.objects.create(therapist=Do1,patient=pa1,Date=Date1,time=T,device=Dev) 
        return redirect('centerapp:Rgetappintmentclinice')      
   

    return render(request, 'Rappointment.html', {'var': 'clAppointments', 'doctors': doctor1, 'sections': sections, 'clinics': clin})

def Rcreateappointment(request):
    doctor1 = Doctor.objects.all()
    sections = Section.objects.all()
    clin = Clinic.objects.all()
    if request.method=="POST":
        iduser=request.POST['pgmail']
        
        idoc=request.POST['doctoe']
        D=request.POST['Date']
        T=request.POST['time']
        print(D)
        print(T)
        # print(iduser)
        # print(idoc)
        # print(appiontment)
        # dname,date_str, start_time_str, end_time_str = appiontment.split(',')

        # date = datetime.strptime(date_str, '%Y-%m-%d').date()
        # start_datetime = datetime.strptime(start_time_str, '%H:%M:%S')
        Do1=Doctor.objects.get(id=idoc)
        pa1=User.objects.get(id=iduser)
        AppointmentDoctor.objects.create(doctor=Do1,patient=pa1,Date=D,time=T) 
        return redirect('centerapp:Rgetappintmentdoctor')      
   

    return render(request, 'Rappointment.html', {'var': 'Appointments', 'doctors': doctor1, 'sections': sections, 'clinics': clin})

def Rcreateappointmentcli(request):
    doctor1 = Doctor.objects.all()
    sections = Section.objects.all()
    clin = Clinic.objects.all()
    if request.method=="POST":
        iduser=request.POST['pgmail']
        
        idoc=request.POST['idDoc']
        de=request.POST['idDev']
        D=request.POST['Date']
        T=request.POST['time'].split(',')[0]
        print(D)
        print(T)
        # print(iduser)
        # print(idoc)
        # print(appiontment)
        # dname,date_str, start_time_str, end_time_str = appiontment.split(',')

        # date = datetime.strptime(date_str, '%Y-%m-%d').date()
        # start_datetime = datetime.strptime(start_time_str, '%H:%M:%S')
        Date1=D.split(',')[1]
        Do1=Therapist.objects.get(id=idoc)
        Dev=Device.objects.get(id=de)
        pa1=User.objects.get(id=iduser)
        Appointmentclinic.objects.create(therapist=Do1,patient=pa1,Date=Date1,time=T,device=Dev) 
        return redirect('centerapp:Rgetappintmentclinice')      
   

    return render(request, 'Rappointment.html', {'var': 'Appointments', 'doctors': doctor1, 'sections': sections, 'clinics': clin})


def Rgetappintmentdoctor(request):
    sections=Section.objects.all()
    clin=Clinic.objects.all()
    apps=AppointmentDoctor.objects.all().order_by('Date')
    print(apps)
    return render(request ,'Rappointment.html',{'var':'Appointments','apps':apps,'sections':sections,'clinics':clin})



def Rshowappointment(request):
    doctor1 = Doctor.objects.all()
    sections = Section.objects.all()
    clin = Clinic.objects.all()
    av_app_date = []
    lav_app_date = []
    if request.method=="POST":
     idDoc = request.POST['idDoc']
     doctor1=Doctor.objects.get(id=idDoc)
     gmailuser=request.POST['pgmail']
     user=User.objects.get(email=gmailuser)
     if user:
      print(idDoc)
      current_date = datetime.now().date()

      day = Daywork.objects.filter(Employ=idDoc).all()
      for l in range(4):
       for i in day:
        if i.code==0:
            dayname="Monday"
        if i.code==1:
            dayname="Tuesday"
        if i.code==2:
            dayname="Wednesday"
        if i.code==3:
            dayname="Thursday"
        if i.code==4:
            dayname="Friday"
        if i.code==5:
            dayname="Saturday"
        if i.code==6:
            dayname="Sunday"                                                                        
        next_day = current_date + timedelta(days=((i.code - current_date.weekday()) % 7)+7*l)

        appointments = AppointmentDoctor.objects.filter(doctor=idDoc, Date=next_day).order_by('time')


        
        start_datetime = datetime.combine(next_day, i.startwork)
        final_datetime = datetime.combine(next_day, i.endwork)        
        finalapppiont = datetime.combine(next_day, time(hour=0, minute=0, second=0))
        finalapppiont1 = datetime.combine(next_day, time(hour=0, minute=0, second=0))
        if appointments:
          for j in appointments:
            finalapppiont=datetime.combine(next_day, j.time)

            j_datetime = datetime.combine(next_day, j.time)  
            print(start_datetime)
            print(j_datetime)
            if j_datetime >= start_datetime + timedelta(minutes=30):
                print('i')
                
                y = f"{dayname},{next_day.strftime('%Y-%m-%d')}/{start_datetime.strftime('%H:%M:%S')},{j_datetime.strftime('%H:%M:%S')}"
                av_app_date.append(y)
                start_datetime = j_datetime + timedelta(minutes=30) 
            else:
                start_datetime = start_datetime+ timedelta(minutes=30) 

          y = f"{dayname},{next_day.strftime('%Y-%m-%d')}/{(finalapppiont+ timedelta(minutes=30)).strftime('%H:%M:%S')},{final_datetime.strftime('%H:%M:%S')}"
          av_app_date.append(y)
        else:
              y = f"{dayname},{next_day.strftime('%Y-%m-%d')}/{i.startwork.strftime('%H:%M:%S')},{i.endwork.strftime('%H:%M:%S')}"
              av_app_date.append(y)   
      print(av_app_date)                    
      for k in av_app_date:
            p1,p2=k.split('/')
          

            dname,date_str= p1.split(',')
            start_time_str, end_time_str = p2.split(',')            

            date = datetime.strptime(date_str, '%Y-%m-%d').date()
            start_datetime = datetime.strptime(start_time_str, '%H:%M:%S')
            end_datetime = datetime.strptime(end_time_str, '%H:%M:%S')

            while end_datetime >= start_datetime + timedelta(minutes=30):
                y = f"{dname},{date.strftime('%Y-%m-%d')}/{start_datetime.strftime('%H:%M:%S')},{(start_datetime + timedelta(minutes=30)).strftime('%H:%M:%S')}"
                print(y)
                lav_app_date.append(y)
                start_datetime = start_datetime + timedelta(minutes=30) 
                
      test1 = []  # Initialize the outer list
      i = 0  # Initialize the outer loop index

      while i < len(lav_app_date):
          test = []
          t1 = lav_app_date[i].split('/')[0]
          print(i)

          j = i
          while j < len(lav_app_date) and lav_app_date[j].split('/')[0] == t1:
              test.append(lav_app_date[j].split('/')[1])
              j += 1

          newdate = {
              'Day': t1,
              'time_sort': test
          }
          test1.append(newdate)

          i = j

      print(test1)

      return render(request, 'Rcreateappointment2.html', {'var': 'Appointments', 'doctor':doctor1,'user':user ,'av_app_date':test1, 'sections': sections, 'clinics': clin})
    
    

    return render(request, 'Rcreateappointment.html', {'var': 'Appointments', 'doctors': doctor1,'av_app_date':lav_app_date, 'sections': sections, 'clinics': clin})


def Rgetpatient(request):
    sections=Section.objects.all()
    clin=Clinic.objects.all()
    pa=User.objects.filter(type='Patient')
    return render(request ,'Rpatient.html',{'var':'patient','patient':pa,'sections':sections,'clinics':clin})

def Rgetpatient1(request,idpa):
    sections=Section.objects.all()
    clin=Clinic.objects.all()
    pat=User.objects.get(id=idpa)
    if request.method=="POST":
        gender=request.POST['gender']
        birthday=request.POST['birthday']
        address=request.POST['address']
        photo=request.FILES.get('photo')
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']   
        print(birthday) 
                         
        pat.name=name
        pat.gender=gender
        pat.birthday=birthday

        pat.address=address
        pat.phone=phone
        pat.email=email
        if photo:
            pat.photo=photo

        pat.save() 
        return redirect('centerapp:Rgetpatient')

    return render(request ,'Rpatient1.html',{'var':'patient','pat':pat,'sections':sections,'clinics':clin})


def Rdeletepatient(request):
    sections=Section.objects.all()
    clin=Clinic.objects.all()
    pa=User.objects.filter(type='Patient')
    if request.method=="POST":
        idpa=request.POST['iddoctor']
        pa=User.objects.get(id=idpa)
        pa.delete()

        return redirect('centerapp:Rgetpatient')
    return render(request ,'Rpatient.html',{'var':'patient','patient':pa,'sections':sections,'clinics':clin})

def Rcreatepatient(request):
    sections=Section.objects.all()
    clin=Clinic.objects.all()
    pa=User.objects.filter(type='Patient')
    if request.method=="POST":
        gender=request.POST['gender']
        birthday=request.POST['birthday']
        address=request.POST['address']
        photo=request.FILES.get('photo')
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']                               

        birthdaydatetime = datetime.strptime(birthday, '%Y-%m-%d').date()

        User.objects.create(name=name,gender=gender,birthday=birthdaydatetime,address=address,phone=phone,email=email,photo=photo,type='Patient')
        return redirect('centerapp:Rgetpatient')

    return render(request ,'Rpatient.html',{'var':'patient','patient':pa,'sections':sections,'clinics':clin})
# ------------------------------------------------------------------------------------------------------------------------
def searchEP(request):
    clin=Clinic.objects.all()
    sections=Section.objects.all()
    if request.method=="POST":
        type1=request.POST['type']
        name1=request.POST['search']
        print(type1)
        print(name1)
        
        if type1=="Patient":

            pat=User.objects.filter(email=name1)
            v1='patient.html'
            v2='patient'
            v3='patient'
            v4=pat
            
        if type1=="Doctors":
            doc=Doctor.objects.filter(name=name1).all()
            v1='Doctor.html'
            v2='Doctors'
            v3='doctors'
            v4=doc
        if type1=="Therapist":
                thi=Therapist.objects.filter(name=name1).all()
                v1='therapist.html'
                v2='Therapist'
                v3='therapist'
                v4=thi
               
    return render(request ,v1,{'var':v2,v3:v4,'sections':sections,'clinics':clin})

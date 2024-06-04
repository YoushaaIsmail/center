from django.urls import path,include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('advice',getadvice,name='getadvice'),
    path('offerapi',getofferapi,name='getofferapi'),
    path('serviceapi',getservice,name='getservice'),
    path('sectionapi',getsectionapi,name='getsectionapi'),          
    path('appiontmenycliniapi',getappiontmenyclinicapi,name='getappiontmenyclinicapi'),

        path('craeteappiontmenycliniapi',creategetappiontmenyclinicapi,name='creategetappiontmenyclinicapi'),        
        path('appintmentdoctorapi',getappintmentdoctorapi,name='getappintmentdoctorapi'),  
                path('createappiontmenydocapi',createappiontmenydocapi,name='createappiontmenydocapi'),
                 path('likenew',creatlikenews,name='creatlikenews'), 
                  path('favordoctor',creatfavordoctor,name='creatfavordoctor'),     
                   path('favorclin',creatfavorclin,name='creatfavorclin'),
                    path('favorther',creatfavorther,name='creatfavorther'),
                    path('CommentCli',creatCommentClir,name='creatCommentClir'), 
                    path('RatingCli',creatRatingCli,name='creatRatingCli'), 
                     path('aboutapi',getaboutapi,name='getaboutapi'),
                     path('MyFaDo',getMyFaDo,name='getMyFaDo'),
                     path('MyFaCl',getMyFaCl,name='getMyFaCl'),
                     path('MyFaThe',getMyFaThe,name='getMyFaThe'),
path('MyappDoBeffor',getMyApDoBefor,name='getMyApDoBefor'),
path('MyApDoAfter',getMyApDoAfter,name='getMyApDoAfter'),
path('MyappClBeffor',getMyApClBefor,name='getMyApClBefor'),
path('MyApClAfter',getMyApClAfter,name='getMyApClAfter'),
path('filtersection/<str:Nseaction>/',getfiltersection,name='getfiltersection'),
path('searchDoctor/<str:Ndoctor>/',searchDoctor,name='searchDoctor'),
path('searchClinic/<str:Nclinic>/',getsearchClinic,name='getsearchClinic'),
path('searchThr/<str:NThe>/',getsearchThr,name='getsearchThr'),
path('searchDev/<str:NDev>/',getsearchDev,name='getsearchDev'),
path('commentCli/<int:idCl>/',getcommentCli,name='getcommentCli'),
path('commentNew/<int:idNe>/',getcommentNew,name='getcommentNew'),
path('updateappiontmenycliniapi',updateappiontmenycliniapi,name='updateappiontmenycliniapi'),
path('updateappiontmenydoapi',updateappiontmenydoapi,name='updateappiontmenydoapi'),
path('getdoctoridapi/<int:idDoc>/',getdoctoridapi,name='getdoctoridapi'),
path('getclinidapi/<int:idcli>/',getclinidapi,name='getclinidapi'),
path('getthiidapi/<int:idthi>/',getthiidapi,name='getthiidapi'),
#  -----------------------------------------------------------
    path('Doctors',getDoctor,name='getDoctor'),
    path('Doctors/<int:pk>/',getDoctorSection,name='getDoctorSection'),
    path('Doctors/creatDoctor/',creatDoctor,name='creatDoctor'), 
     path('getdoc1/<int:iddoc>/',getdoc1,name='getdoc1'),
    path('Doctors/edit',editDoctor,name='editDoctor'),
    path('Doctors/delete',deletedoctoer,name='deletedoctoer'),
#  -----------------------------------------------------------------
    path('therapist',getthis,name='getthis'),
    path('therapist/creattherapist/',creattherapist,name='creattherapist'),
    path('therapist/deletetherapist/',deletethi,name='deletetherapist'),
    path('therapist1/<int:idth>/',getthis1,name='getthis1'),
    path('therapist/<int:pk>/',getthisClin,name='getthisClin'),
#  -----------------------------------------------------------------   
    path('Diveces',getDiv,name='getDiv'),
    path('Diveces/<int:pk>/',getDivClin,name='getDivClin'),
    path('Diveces/creatDevice/',creatDevice,name='creatDevice'),
    path('Diveces/deleteDevice/',deleteDevice,name='deleteDevice'),
        path('Diveces1/<int:idDev>/',getDev1,name='getDev1'),
#  -----------------------------------------------------------------   
    path('Recaptions',getRec,name='getRec'),

    path('Recaptions/creatRecaptions/',creatRecaptions,name='creatRecaptions'),
    path('Recaptions/deleteRecaptions/',deleteRecaptions,name='deleteRecaptions'),
    path('Recaptions1/<int:idRe>/',getRec1,name='getRec1'),        
#  -----------------------------------------------------------------

    path('News',getNews,name='getNews'),
    path('News/<int:idnew>/',getNews1,name='getNews1'),
    path('News/createNews/',createNews,name='createNews'),
    path('News/deleteNews/',deleteNews,name='deleteNews'),
#  -----------------------------------------------------------------
    path('patients',getpatient,name='getpatient'),
    path('patients/<int:idpa>/',getpatient1,name='getpatient1'),
    path('patients/createpatient/',createpatient,name='createpatient'),
    path('patients/deletepatient/',deletepatient,name='deletepatient'),

#  -----------------------------------------------------------------
    path('Sections',getsection,name='getsection'),
    path('Sections/<int:idsec>/',getsection1,name='getsection1'),
    path('Sections/createSection/',createSection,name='createSection'),
    path('Sections/deleteSection/',deletesection,name='deletesection'),
    
#  -----------------------------------------------------------------
    path('Clinics',getclinic,name='getclinic'),
    path('Clinics/<int:idcli>/',getclinic1,name='getclinic1'),
    path('Clinics/createclin/',createclin,name='createclin'),
    path('Clinics/deleteclin/',deleteclin,name='deleteclin'),
    
#----------------------------------------------------------------------------- 
    path('staiteces',getstaiteces,name='getstaiteces'),
# ----------------------------------------------------------------------------
    path('Daywork',getdaywork,name='getdaywork'),
    path('Daywork/delete',deleteDaywork,name='deleteDaywork'),
    path('Daywork/craete',createDaywork,name='createDaywork'),
        path('Daywork1/<int:idDay>/',getDaywork1,name='getDaywork1'),
# ----------------------------------------------------------------------------
    path('appointmentDoctors',getappintmentdoctor,name='getappintmentdoctor'),
    path('appointment',showappointment,name='showappointment'),
    path('appointment/deleteappointment/',deleteappiontmentdoctor,name='deleteappiontmentdoctor'),
    path('createappointment',createappointment,name='createappointment'),
    # ---------------------------------------------------------------------------
    path('offer',getoffer,name='getoffer'),
    path('offer1/<int:idoff>',showoffer,name='showoffer'),
    path('offer/deleteoffer/',deleteoffer,name='deleteoffer'),
    path('createoffer',createoffer,name='createoffer'),
    # ------------------------------------------------------------------------------
    path('appintmentclinice',getappintmentclinice,name='getappintmentclinice'),
    path('appointmentcli',showappointmentcli,name='showappointmentcli'),
    path('appointmentcli/deleteappointmentcli/',deleteappiontmentcli,name='deleteappiontmentcli'),
    path('createappointmenclit',createappointmentcli,name='createappointmentcli'),
    # ---------------------------------------------------------------------------
    path('home',home,name='home'),
    path('login',login1,name='login'), 
# --------------------------------------------------------------------------------------------------
    path('Rappintmentclinice',Rgetappintmentclinice,name='Rgetappintmentclinice'),
    path('Rappointmentcli',Rshowappointmentcli,name='Rshowappointmentcli'),
    path('Rappointmentcli/deleteappointmentcli/',Rdeleteappiontmentcli,name='Rdeleteappiontmentcli'),
    path('Rcreateappointmenclit',Rcreateappointmentcli,name='Rcreateappointmentcli'),

    path('RappointmentDoctors',Rgetappintmentdoctor,name='Rgetappintmentdoctor'),
    path('Rappointment',Rshowappointment,name='Rshowappointment'),
    path('Rappointment/deleteappointment/',Rdeleteappiontmentdoctor,name='Rdeleteappiontmentdoctor'),
    path('Rcreateappointment',Rcreateappointment,name='Rcreateappointment'),

        path('Rpatients',Rgetpatient,name='Rgetpatient'),
    path('Rpatients/<int:idpa>/',Rgetpatient1,name='Rgetpatient1'),
    path('Rpatients/createpatient/',Rcreatepatient,name='Rcreatepatient'),
    path('Rpatients/deletepatient/',Rdeletepatient,name='Rdeletepatient'),

    # -----------------------------------------------------------------------------------------------
path('getmap',getmap,name='getmap'),
path('getabout',getabout,name='getabout'),
path('getabout1/<int:idab>/',Editabout,name='Editabout'),
path('getchat',getchat,name='getchat'),
path('editeuser',editeuser,name='editeuser'),
path('searchEP',searchEP,name='searchEP'),

path('editeuser',editeuser,name='editeuser'),
path('editeuser',editeuser,name='editeuser'),
    path('send/' , send,name='send'),
    path('firebase-messaging-sw.js',showFirebaseJS,name="show_firebase_js"),
    path('notf',notf,name="notf"),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

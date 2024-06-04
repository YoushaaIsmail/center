from django.urls import path,include
from dj_rest_auth.views import UserDetailsView
from dj_rest_auth.views import UserDetailsView
from .serializers import Users2
from .views import NewloginView
from dj_rest_auth.views import LoginView
urlpatterns = [
    path('registration/',include('dj_rest_auth.registration.urls')),
    path('profile/', include('allauth.urls')),
        path('profile1/', include('dj_rest_auth.urls')),
    path('Newlogin/',LoginView.as_view(),name='login'),
    path('user/', UserDetailsView.as_view(serializer_class=Users2))]






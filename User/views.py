from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from dj_rest_auth.views import LoginView
# Create your views here.

class NewloginView(LoginView):
    def get_response(self):
        response = super().get_response()

        if response.status_code == status.HTTP_200_OK:
            user = self.user
            if user.is_verified:
                token = response.data['key']
                return Response({
                    'status': status.HTTP_200_OK,
                    'message': 'Login successful',
                    'data': {
                        'key': token
                    }
                })
            else:
                return Response({
                    'status': status.HTTP_401_UNAUTHORIZED,
                    'message': 'User is not verified',
                    'data': None
                })
        return response
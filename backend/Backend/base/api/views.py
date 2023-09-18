from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import NoteSerializer
from base.models import Note

from rest_framework.permissions import IsAuthenticated 


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username #tableau crypted
        # ...
        return token
    


    



class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class=MyTokenObtainPairSerializer



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getNotes(request):
    user=request.user  #get the user from the request
    notes=user.note_set.all()   #get only the notes from the exact user
    serializer=NoteSerializer(notes,many=True)    
    return Response(serializer.data)





@api_view(['GET'])
def getroutes(request):
    routes=[
        'api/tocken', #route where you submit a username and password and get a acces tocken and a refresh tocken
        'api/tocken/refresh' #give you a new tocken based on the tocken that you sent to the backend
    ]
    return Response(routes)
# Create your views here.

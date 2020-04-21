from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

# Create your views here.

class UserAPIView(APIView):
    """ APIView for managing user profiles """
    
    serializer_class = serializers.UserSearializer
    
    def get(self, request, format=None):
        """ method for handling get request to this class """

        an_apiview = [
        'lalala',
        ':P:P:P',
        ':D:D:D',
        ]
        return Response({'about' : 'Hello there ','content' : an_apiview, 'reaction' : 'finally full stack'})
        
    def post(self, request):
        """ method handling the post requests to this view """
        
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            #message_string = f'Hello {serializer.validated_data.get('name')} you are {serializer.validated_data.get('age')} years old'
            
            name = serializer.validated_data.get('name')
            age = serializer.validated_data.get('age')
            message_string = 'Hello ' + name + " you are " + str(age) + " years old"
            return Response({'message' : message_string})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )
                
        
                           
    
        
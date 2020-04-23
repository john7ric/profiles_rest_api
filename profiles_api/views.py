from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets

# Create your views here.

class UserAPIView(APIView):
    """ APIView for managing user profiles """
    
    serializer_class = serializers.UserSearializer
    
    def get(self, request, format=None):
        """ method for handling get request to this class """

        an_apiview = [
        'This is an API View Class',
        'We can write http requests like Post, get , put, patch and delete',
        'Urls are created in urls.py of the api app , creates using path() ',
        'This is used when full control is needed in the API logic',
        'Lets have a look, shall we ?'
        ]
        return Response({'about' : 'Hello there ','content' : an_apiview})
        
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


    def patch(self, request, pk=None):
        """ method for handling patch requests to this class"""

        return Response({'method' : 'Patch'})


    def put(self, reaction, pk=None):
        """method for handling put"""

        return Response({'message': 'PUT'})

    def delete(self, request, pk=None):
        """method to handle delete"""

        return Response({'message' : 'Delete'})        
                
                
        


class HelloViewSet(viewsets.ViewSet):
    """ Test ViewSet Class """


    serializer_class = serializers.UserSearializer

    def list(self, request):
        a_viewset = [
            'this is a viewset class',
            'which can perform a lot of functions with very less code',
            'also maps automatically to URLs using routers',
            "Hmm thats interestinf , isn't it ",
            'so lets go',
            'lets have a look',
        ]
        return Response({'message' : 'Yes boi', 'list' : a_viewset})


    def create(self,request):
        """ to create a new object """

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            age = serializer.validated_data.get('age')

            return Response({'message' : f'Hello {name} you are {age} years old'})

        else:
             return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST) 


    def retrieve(self, request,pk=None) :
         """ doc string to fetch an object with an ID"""
         return Response({'message' : 'retreive is called'})        


    def update(self,request, pk=None):
        """ method to update a view """

        return Response({'message' : 'methode called is update'})   


    def partial_update(self, request, pk=None):
        """method for partial update """     

        return Response({'Message' : 'Method patch'})


    def destroy(self, request , pk=None):
        """ method to delete the object with ID"""

        return Response({'message' : 'HTTP Delete'})



from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class UserAPIView(APIView):
    """ APIView for managing user profiles """
    def get(self, request, format=None):
        """ method for handling get request to this class """

        an_apiview = [
        'lalala',
        ':P:P:P',
        ':D:D:D',
        ]
        return Response({'about' : 'Hello there ','content' : an_apiview, 'reaction' : 'finally full stack'})
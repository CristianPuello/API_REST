from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
import requests
from rest_framework.response import Response
from rest_framework import status
from .models import Jokes
from .serializers import JokeSerializer

class JokePagination(PageNumberPagination):
    page_size = 5
    max_page_size = 10

class JokeList(APIView):
    serializer_class = JokeSerializer
    pagination_class = JokePagination()


    def get(self, request):
        nombre = request.query_params.get('nombre')
        paginate = request.query_params.get('paginate')
        if nombre == 'Chuck':
            url = 'https://api.chucknorris.io/jokes/random'
            response = requests.get(url)
            joke = response.json()['value']
            return Response({'joke': joke}, status=status.HTTP_200_OK)
    
        else:
            if paginate == 'true':
                joke = Jokes.objects.all()
                page = self.pagination_class.paginate_queryset(joke, request)
                serializer = JokeSerializer(page, many=True)
                return self.pagination_class.get_paginated_response(serializer.data)
            else:
                joke = Jokes.objects.all()
                serializer = JokeSerializer(joke, many = True)
                return Response({'joke':serializer.data}, status=status.HTTP_200_OK)
           
            
    def post(self, request):
        data = request.data
        text = Jokes.objects.create(
            joke = data['joke']
        )
        serializer = JokeSerializer(text, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def put(self, request, pk):
        joke  = Jokes.objects.get(id = pk)
        serializer = JokeSerializer(joke, data = request.data)   
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)     
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, pk):
        joke = Jokes.objects.get(id = pk)
        joke.delete()
        return Response('Joke Delete', status= status.HTTP_200_OK)
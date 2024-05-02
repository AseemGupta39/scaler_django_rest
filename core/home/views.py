# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.models import Person
from home.serializers import PeopleSerializer

@api_view(['GET','POST'])
def index(request):
    courses = {'course_name':'python',
               'topic':['flask','fastapi','django'],
               'teacher':'abhijeet bhaiya'}
    if request.method == 'GET':
        print('get method called')
        data = request.GET.get('search')
        print(f'\n\n\n\n\n{data}\n\n\n\n\n')

    elif request.method == 'POST':
        data = request.data
        print(f'\n\n\n\n\n{data} and to be specific {data['name']}\n\n\n\n\n')
        print('post method called')
    else:
        print('ran into some problem')
    return Response(courses)
# Create your views here.

@api_view(['GET','POST'])
def people(request):
    if request.method == 'GET':
        objs = Person.objects.all()
        serializer = PeopleSerializer(objs,many = True)
        return Response(serializer.data)
    else: # post method
        data = request.data
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET','POST'])
def index(request):
    courses = {'course_name':'python',
               'topic':['flask','fastapi','django'],
               'teacher':'abhijeet bhaiya'}
    if request.method == 'GET':
        print('get method called')
    elif request.method == 'POST':
        print('post method called')
    else:
        print('ran into some problem')
    return Response(courses)
# Create your views here.

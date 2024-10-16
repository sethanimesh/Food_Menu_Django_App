from django.http import HttpResponse
from django.shortcuts import render

from food.models import Item

def index(request):
    item_list = Item.objects.all()
    return HttpResponse(item_list)
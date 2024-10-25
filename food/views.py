from django.http import HttpResponse
from django.shortcuts import render

from food.models import Item

def index(request):
    item_list = Item.objects.all()
    context = {'item_list':item_list,}
    return render(request, 'food/index.html', context)

def detail(request, item_id):
    return HttpResponse("Item is %d"%item_id)
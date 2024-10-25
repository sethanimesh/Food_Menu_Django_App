from django.urls import path
from food import views

app_name = 'food'
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:item_id>/", views.detail, name="detail")
]
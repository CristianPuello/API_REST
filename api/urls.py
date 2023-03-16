from django.urls import path
from .views import JokeList

urlpatterns = [
    path('', JokeList.as_view()),
    path('<int:pk>', JokeList.as_view())
]

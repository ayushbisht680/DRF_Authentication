from django.urls import path
from .views import getit,postit,putit,deleteit,StudentAPI,RegisterAPI



urlpatterns = [
    # path('get/', getit),
    # path('post/', postit),
    # path('put/<id>', putit),
    # path('delete/<id>', deleteit),
    path('student/',StudentAPI.as_view()),
    path('register/',RegisterAPI.as_view())
]
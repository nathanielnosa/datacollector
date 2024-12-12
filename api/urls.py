from django.urls import path
from . import views
urlpatterns=[
    path('register/',views.RegisterView.as_view()),
    path('entry/',views.DataFieldView.as_view()),
    path('entry/<str:pk>/',views.UpdateDataFieldView.as_view())
]
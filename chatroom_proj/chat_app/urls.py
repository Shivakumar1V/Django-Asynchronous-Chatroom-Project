from django.urls import path
from chat_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chat/<str:room_name>/', views.chatRoom, name='chatRoom'), 
    path('login/', views.loginHandler, name='loginHandler'),
    path('signup/', views.signupHandler, name='signupHandler'),
    path('logout/', views.logoutHandler, name='logoutHandler'),
]

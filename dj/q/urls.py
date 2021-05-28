from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('login/', views.index, name='index'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('create_user/', views.createUser, name='create_user'),
]
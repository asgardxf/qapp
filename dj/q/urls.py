from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('create_user/', views.createUser, name='create_user'),
]

for key in views.urlMap:
	urlpatterns.append(path(key, views.urlMap[key]))
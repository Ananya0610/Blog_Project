from django.urls import path,include
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('home',views.home,name='home'),
    path('signup', views.signup, name='signup'),
    path('create-post',views.create_post,name='createpost'),
    # path('login/',views.login,name="login"),
]

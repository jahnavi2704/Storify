from django.urls import path,re_path
from django.conf.urls import include , url
from . import views
from django.contrib.auth import views as auth_views

from rest_framework.routers import DefaultRouter , SimpleRouter

#router=routers.SimpleRouter()

urlpatterns = [

    url(r'^$', views.usersignup, name='register_user'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate_account, name='activate'),
    path('login/',auth_views.LoginView.as_view(template_name = 'mainapp/login1.html'),name = 'login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'mainapp/login.html'),name = 'logout'),
    path('home/', views.homepage, name='homepage'),
    path('detail/',views.detail_article, name="detail"),
	path('storecom/',views.comments_show, name="storecom"),
	path('profile/', views.UpdateProfile, name="profile"),
    url(r'^articles_api/$',views.articlelist, name="articlelist" ),

    #path('api-auth/',include('rest_framework.urls',namespace='rest_framework'))
	#path('genre/',views.genre_display, name="genre")
    
    #path("<slug:slug>/", views.articleDetailView.as_view(), name="detail"),

]				



from django.contrib import admin
from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index,name="index"),
    path('bought',views.bought,name="bought"),
    path('sendmainn',views.sendmainn,name="sendmainn"),

    path('loginuser',views.loginuser,name="loginuser"),
    path('signupuser',views.signupuser,name="signupuser"),
    path('logoutuser',views.logoutuser,name="logoutuser"),
    path('mainn',views.mainn,name="mainn"),
    path('<int:pk>/',views.detail,name="detail"),
    path('sold/<int:pk>/',views.sold,name="sold"),
    path('search/',views.search,name="search"),
    path('sell',views.sell,name="sell"),
    path('<int:pk>/sendmainn/', views.sendmainn, name="sendmainn"),
    



]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

appname= 'bldon'
urlpatterns=[

path('',views.index, name= 'main'),
path('register/', views.donorregister,name = 'register'),
path('eligible/', views.eligible, name = 'eligible'),
path('setappointment/', views.app, name = 'appointment'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='index'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),

    path('person/', views.person_list, name='person_list'),
    path('person/new/', views.person_create, name='person_create'),
    path('person/<str:userID>/', views.person_detail, name='person_detail'),
    path('person/<str:userID>/edit/', views.person_edit, name='person_edit'),
    path('person/<str:userID>/delete/', views.person_delete, name='person_delete'),

    path('certificate/', views.certificate_list, name='certificate_list'),
    path('certificate/<int:certNumber>/', views.certificate_detail, name='certificate_detail'),
    path('certificate/new/', views.certificate_create, name='certificate_create'),
    path('certificate/<int:certNumber>/edit/', views.certificate_edit, name='certificate_edit'),
    path('certificate/<int:certNumber>/delete/', views.certificate_delete, name='certificate_delete'),
]



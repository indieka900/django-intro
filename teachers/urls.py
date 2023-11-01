from django.urls import path
from . import views

app_name = "teachers"

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('add/', views.add, name='add' ),
    path('viewdata/',views.viewData, name='viewdata'),
    path('delete/<id>', views.delete, name='delete'),
    path('edit/<id>', views.edit, name='edit'),
]
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    ClientListView,
    ClientUpdateView,
    ClientDetailView,
    ClientDeleteView,
    ClientCreateView

)



urlpatterns = [

    path('<int:pk>/edit/',
         ClientUpdateView.as_view(), name='client_edit'),
    path('<int:pk>/',
         ClientDetailView.as_view(), name='client_detail'),
    path('<int:pk>/delete/',
         ClientDeleteView.as_view(), name='client_delete'),
    path('', ClientListView.as_view(), name='client_list'),
    path('new/', ClientCreateView.as_view(), name='client_new'),

    path('<int:pk>/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),


]

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.LoginView.as_view(), name="login"),
    path('add_blank/', views.CreateBlankView.as_view(), name='add_blank'),
    path('salary/', views.ListBlankView.as_view(), name='list_blank'),
    path('salary/filter/', views.FilterView.as_view(), name='filter'),
    path('monitoring/', views.BlankMonitoringView.as_view(success_url="/monitoring/"), name='monitor_blank'),
    path('monitoring/blank_update/<int:pk>', views.BlankUpdateView.as_view(), name='update_blank'), 
    path('monitoring/blank_delete/<int:pk>', views.BlankDeleteView.as_view(), name='delete_blank'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]

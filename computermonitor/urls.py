from django.urls import path

from . import views

app_name = 'computermonitor'


urlpatterns = [
     path('',views.MainIndexView.as_view(), name='index'),
     path('computers/',views.ComputerListView.as_view(),name='computer_list'),
     path('computerbackups/',views.ComputerBackupListView.as_view(),name='computer_backuplist'),
     path('computers/<int:pk>', views.ComputerDetailView.as_view(), name='computer_detail'),
     path('computers/<int:pk>/remove/', views.ComputerDeleteView.as_view(), name='computer_remove'),
     path('computers/<int:pk>/edit/', views.ComputerUpdateView.as_view(), name='computer_edit'),
     path('computers/new/', views.CreateComputerView.as_view(), name='computer_new'),
     path('accounts/profile/',views.MainIndexView.as_view(), name='profile'),
     path('computerbackups/<int:pk>/remove/', views.ComputerBackupDeleteView.as_view(), name='computerbackup_remove'),
     path('computerbackups/detaillist/',views.computerbackupdetail,name='computer_backuplist_detail'),
     path('computerbackups/computerlistdetail/',views.computerlistdetail,name='computer_list_detail'),
     path('computerbackups/<int:pk>/removeall/', views.removeComputerBackups, name='computerbackup_remove_all'),
     path('computerbackups/removeall/', views.removeAllBackups, name='remove_all_computerbackups'),

]
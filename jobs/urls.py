from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job-list'),
    path('jobs/<int:pk>/', views.job_detail, name='job-detail'),
    path('jobs/<int:pk>/update/', views.JobUpdateView.as_view(), name='job-update'),
    path('jobs/<int:pk>/delete/', views.JobDeleteView.as_view(), name='job-delete'),
    path('jobs/<int:pk>/apply/', views.apply_for_job, name='apply-for-job'),
]
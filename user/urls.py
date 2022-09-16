from django.urls import path
from rest_framework.authtoken import views as auth_views

from user import views

urlpatterns=[
    path('token-auth/', auth_views.obtain_auth_token),
    path('student/get',views.ListStudentsDetails.as_view()),
    path('student/<int:pk>',views.StudentDetail.as_view()),
    path('student/create',views.CreateStudentDetails.as_view()),
    path('student/update/<int:pk>',views.UpdateStudentDetails.as_view()),
    path('student/delete/<int:pk>',views.DeleteStudentDetails.as_view()),

]
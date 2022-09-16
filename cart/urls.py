from django.urls import path
from cart import views


urlpatterns =[
    path('create/', views.CreateCheckout.as_view()),
    path('list/', views.ListCheckouts.as_view()),
    path('<int:pk>/', views.ListCheckout.as_view()),
    path('update/<int:pk>/', views.UpdateCheckoutDetails.as_view()),
    path('delete/<int:pk>/', views.DeleteCheckout.as_view()),
]
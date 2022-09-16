from django.urls import path
from book import views


urlpatterns = [
    path('create/', views.CreateBookDetails.as_view()),
    path('list/', views.ListBooks.as_view()),
    path('<int:pk>/',views.ListBook.as_view()),
    path('update/<int:pk>/',views.UpdateBookDetails.as_view()),
    path('delete/<int:pk>/',views.DeleteBook.as_view()),

]
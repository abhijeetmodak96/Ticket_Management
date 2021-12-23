from django.urls import path, include
from api import views

urlpatterns = [
    path('tickets/', views.TicketList.as_view()),
    path('tickets/<int:pk>/', views.TicketDetail.as_view()),
    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>/', views.CommentDetail.as_view()),
]

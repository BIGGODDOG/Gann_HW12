from django.urls import path
from .views import BookAPIView, BookDetailAPIView

urlpatterns = [
    path('books/', BookAPIView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),
]

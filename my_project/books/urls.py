from django.urls import path
from .views import BookAPIView, BookDetailAPIView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookListCreateView, BookDetailView

router = DefaultRouter()
router.register('books', BookViewSet, basename='book')
router.register('list', BookListCreateView, basename='list')
router.register('detail', BookDetailView, basename='detail')

urlpatterns = [
    path('books/', BookAPIView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),
    path('drf/', include(router.urls)),
]

from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import BookListApiView, BookDetailApiView, BookUpdateApiView,\
    BookDeleteApiView, BookListCreateApiView, BookCreateApiView, BookDetailDeleteApiView, \
    BookUpdateDeleteApiView, BookDetailUpdateDeleteApiView, BookViewset

router = SimpleRouter()
router.register('books', BookViewset, basename='books')

urlpatterns = [
    # path('books/', BookListApiView.as_view(),),
    # path('books/create/', BookCreateApiView.as_view()),
    # path('book/', BookListCreateApiView.as_view(),),
    # path('books/<int:pk>/delete/', BookDeleteApiView.as_view()),
    # path('books/<int:pk>/update/', BookUpdateApiView.as_view()),
    # path('books/<int:pk>/updatedelete/', BookUpdateDeleteApiView.as_view()),
    # path('books/<int:pk>/', BookDetailApiView.as_view(),),
    # path('book/<int:pk>/detaildelete',BookDetailDeleteApiView.as_view()),
    # path('bookupdatedelete/<int:pk>/', BookDetailUpdateDeleteApiView.as_view()),
]

urlpatterns += router.urls


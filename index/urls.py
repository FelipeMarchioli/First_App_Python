from django.urls import include, path
from . import views

urlpatterns = [
  path('', views.welcome),
  path('getbooks/<str:headquarter>', views.get_books),
  path('addbook', views.add_book),
  path('deletebook', views.delete_book),
  path('updatebook', views.update_book)
]
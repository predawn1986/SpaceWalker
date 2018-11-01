from django.conf.urls import url, include
from uiauto import views
urlpatterns = [
    url(r'add_book$', views.add_book, ),
    url(r'show_books$', views.show_books, ),
]
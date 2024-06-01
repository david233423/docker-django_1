from django.urls import path

from .views import home_pages_view

urlpatterns = [
	path( "" , home_pages_view , name="home")
]

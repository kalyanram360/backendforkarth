from django.urls import path
from . import views

urlpatterns = [
    path('api/data/', views.get_data, name='get_data'),  # GET route
    path('api/data/create/', views.create_item, name='create_item'),  # POST route
]

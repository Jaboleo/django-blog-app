from django.urls import path
from .views import HomePageView, PostsView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('posts', PostsView.as_view(), name='posts')
]



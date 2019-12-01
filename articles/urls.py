from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('posts/new', views.post_new, name='post_new'),
    path('posts/<int:pk>', views.PostDetailsView.as_view(), name='post_details'),
    path('posts/<int:pk>/edit', views.PostEditView.as_view(), name='post_edit'),
    path('posts/<int:pk>/delete', views.PostDeleteView.as_view(), name='post_delete')
]



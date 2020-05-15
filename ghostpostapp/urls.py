from django.urls import path
from ghostpostapp import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('post/', views.createpost),
    path('upvote/<int:id>/', views.up_votes),
    path('downvote/<int:id>/', views.down_votes),
    path('boasts/', views.boast, name='boast'),
    path('roasts/', views.roast, name='roast'),
    path('sorted/', views.sortedby_posts)
]

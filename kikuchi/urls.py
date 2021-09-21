from django.urls import path
from . import views


app_name = 'kikuchi'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
    path('blog_list/', views.BlogListView.as_view(), name="blog_list"),
    path('blog_detail/<int:pk>/', views.BlogDetailView.as_view(), name="blog_detail"),
    path('blog_create/', views.BlogCreateView.as_view(), name="blog_create"),
    path('blog_update/<int:pk>/', views.BlogUpdateView.as_view(), name="blog_update"),
    path('blog_delete/<int:pk>/', views.BlogDeleteView.as_view(), name="blog_delete"),
]
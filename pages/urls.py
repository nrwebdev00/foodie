from django.urls import path
from . import views


urlpatterns = [
  path('', views.home_page, name='home'),

  path('quick_idea/<slug:idea>/', views.quick_ideas, name='quick_idea'),

  path('courses/', views.courses_page, name='courses'),
  path('courses/<str:course>/', views.course_page, name='course'),
]
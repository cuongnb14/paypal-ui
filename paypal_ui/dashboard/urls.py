from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('active-plan/<str:plan_id>', views.active_plan, name='active_plan'),
]

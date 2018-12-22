from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('active-plan/<str:plan_id>', views.active_plan, name='active_plan'),
    path('delete-plan/<str:plan_id>', views.delete_plan, name='delete_plan'),
    path('plan/<str:plan_id>', views.plan_detail, name='plan_detail'),
]

from django.urls import path, include

from app.views import StartPage, TaskPage, TaskDetail, TaskUpdate

urlpatterns = [
    path('', StartPage.as_view(), name='start'),
    path('tasks/', TaskPage.as_view(), name='task'),
    path('tasks/<slug:slug_param>/', TaskDetail.as_view(), name='detail'),
    path('tasks/<slug:slug_param>/update/', TaskUpdate.as_view(), name='update')
]
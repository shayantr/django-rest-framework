"""
URL configuration for drf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include

from todo.views import todos_json, todo_detail_view, ManageTodoApiView, TodosDetailApiView, TodosListMixinApiView, \
    TodosDetailMixinApiView, TodoListGenericsApiView, TodoDetailGenericsApiView, TodoViewsetApi, UserViewsetApi

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('todos', TodoViewsetApi)
router.register('users', UserViewsetApi)

urlpatterns = [
    path('', todos_json),
    path('<int:todo_id>', todo_detail_view),
    path('cbv/', ManageTodoApiView.as_view()),
    path('cbv/<int:todo_id>', TodosDetailApiView.as_view()),
    path('mixins/', TodosListMixinApiView.as_view()),
    path('mixins/<int:pk>', TodosDetailMixinApiView.as_view()),
    path('generics/', TodoListGenericsApiView.as_view()),
    path('generics/<int:pk>', TodoDetailGenericsApiView.as_view()),
    path('viewsets/', include(router.urls)),
]

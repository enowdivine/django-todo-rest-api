from todos.views import (
    CreateTodoAPIView,
    TodoListAPIView,
    TodosAPIView,
    TodoDetailsAPIView,
)
from django.urls import path

urlpatterns = [
    # path("create", CreateTodoAPIView.as_view(), name="create-todo"),
    # path("list", TodoListAPIView.as_view(), name="list-todo"),
    path("", TodosAPIView.as_view(), name="todos"),
    path("<int:id>", TodoDetailsAPIView.as_view(), name="todo"),
]

from django.urls import path

from todotasks.views import (
    TaskListView,
    TagListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView, change_task_completion_status,
)

urlpatterns = [
    path("",
         TaskListView.as_view(),
         name="task-list"),
    path("task/create/",
         TaskCreateView.as_view(),
         name="task-create"),
    path("task/<int:pk>/update/",
         TaskUpdateView.as_view(),
         name="task-update"),
    path("task/<int:pk>/delete/",
         TaskDeleteView.as_view(),
         name="task-delete"),
    path("tags/",
         TagListView.as_view(),
         name="tag-list"),
    path("tags/create/",
         TagCreateView.as_view(),
         name="tag-create"),
    path("tags/<int:pk>/update/",
         TagUpdateView.as_view(),
         name="tag-update"),
    path("tags/<int:pk>/delete/",
         TagDeleteView.as_view(),
         name="tag-delete"),
    path("<int:pk>/change_task_completion_status/",
         change_task_completion_status,
         name="change-task-completion-status"),
]

app_name = "todotasks"

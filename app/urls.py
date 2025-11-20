from django.urls import path
from .views import (
    BookmarkListView,
    BookmarkDetailView,
    BookmarkCreateView,
    BookmarkUpdateView,
    BookmarkDeleteView,
)

urlpatterns = [
    path("", BookmarkListView.as_view(), name="bookmark_list"),
    path("create/", BookmarkCreateView.as_view(), name="bookmark_create"),
    path("<int:pk>/", BookmarkDetailView.as_view(), name="bookmark_detail"),
    path("<int:pk>/update/", BookmarkUpdateView.as_view(), name="bookmark_update"),
    path("<int:pk>/delete/", BookmarkDeleteView.as_view(), name="bookmark_delete"),
]

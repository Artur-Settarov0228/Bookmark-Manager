from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Bookmark


class BookmarkListView(LoginRequiredMixin, ListView):
    model = Bookmark
    template_name = "bookmarks/bookmark_list.html"
    context_object_name = "bookmarks"

    def get_queryset(self):
        queryset = Bookmark.objects.filter(user=self.request.user)

        # Search
        q = self.request.GET.get("q")
        if q:
            queryset = queryset.filter(title__icontains=q)

        # Tag filter
        tag = self.request.GET.get("tag")
        if tag:
            queryset = queryset.filter(tags__name=tag)

        return queryset.order_by("-created_at")


class BookmarkDetailView(LoginRequiredMixin, DetailView):
    model = Bookmark
    template_name = "bookmarks/bookmark_detail.html"
    context_object_name = "bookmark"

    def get_queryset(self):
        # Faqat o'zining bookmarklarini ko'rish
        return Bookmark.objects.filter(user=self.request.user)

class BookmarkCreateView(LoginRequiredMixin, CreateView):
    model = Bookmark
    fields = ["title", "url", "description", "tags"]
    template_name = "bookmarks/bookmark_form.html"
    success_url = reverse_lazy("bookmark_list")

    def form_valid(self, form):
        # Bookmarkni userga biriktiramiz
        form.instance.user = self.request.user
        return super().form_valid(form) 

class BookmarkUpdateView(LoginRequiredMixin, UpdateView):
    model = Bookmark
    fields = ["title", "url", "description", "tags"]
    template_name = "bookmarks/bookmark_form.html"
    success_url = reverse_lazy("bookmark_list")

    def get_queryset(self):
        # Faqat o'zining bookmarklarini tahrirlashga ruxsat beradi
        return Bookmark.objects.filter(user=self.request.user)



class BookmarkDeleteView(LoginRequiredMixin, DeleteView):
    model = Bookmark
    template_name = "bookmarks/bookmark_confirm_delete.html"
    success_url = reverse_lazy("bookmark_list")

    def get_queryset(self):
        # Faqat o'zining bookmarklarini o'chirishga ruxsat beradi
        return Bookmark.objects.filter(user=self.request.user)



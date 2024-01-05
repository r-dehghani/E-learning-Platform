from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Course
from django.views.generic.list import ListView


class ManageCourseListView(ListView):
    model = Course
    template_name = 'courses/manage/course/list.html'

    def get_queryset(self) -> QuerySet[Any]:
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)
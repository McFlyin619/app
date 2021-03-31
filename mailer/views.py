#-*- coding: utf-8 -*-
from django.db.models.query import Prefetch
from django.shortcuts import render
from django.views.generic import ListView
from mailer.models import Company
class IndexView(ListView):
    template_name = "mailer/index.html"
    model = Company
    paginate_by = 100


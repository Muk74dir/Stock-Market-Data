from django.shortcuts import render
from django.views.generic import View
from .models import JSONModel



class HomeView(View):
    context = {}
    def get(self, request):
        all_data = JSONModel.objects.all()
        self.context['all_data'] = all_data
        return render(request, 'index.html', self.context)
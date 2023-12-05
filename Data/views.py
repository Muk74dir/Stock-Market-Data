from django.shortcuts import render, redirect
from django.views.generic import View
from .models import JsonToSQLModel
from .forms import EditForm


class HomeView(View):
    context = {}
    def get(self, request):
        all_data = JsonToSQLModel.objects.all()
        self.context['all_data'] = all_data
        return render(request, 'index.html', self.context)
    
class EditView(View):
    context = {}
    def get(self, request, pk):
        data = JsonToSQLModel.objects.get(pk=pk)
        form = EditForm(instance=data)
        self.context['form'] = form
        return render(request, 'edit.html', self.context)
    
    def post(self, request, pk):
        data = JsonToSQLModel.objects.get(pk=pk)
        form = EditForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
        else:
            self.context['form'] = form
            return render(request, 'edit.html', self.context)
        return redirect('index')
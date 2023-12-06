from django.shortcuts import render, redirect
from django.views.generic import View
from .models import JsonToSQLModel
from .forms import EditForm, TradeSearchFrom


class HomeView(View):
    context = {}
    def get(self, request):
        all_data = JsonToSQLModel.objects.all()
        self.context['all_data'] = all_data
        trade_codes = list(JsonToSQLModel.objects.values_list('trade_code', flat=True).distinct())
        charts_data = []
        for trade_code in trade_codes:
            queryset = JsonToSQLModel.objects.filter(trade_code=trade_code)
            data = {
                'trade_code': trade_code,
                'dates': [entry.date.strftime('%y-%m-%d') for entry in queryset],
                'close_dates': [str(entry.close) for entry in queryset],
                'volume_dates': [entry.volume for entry in queryset],
            }
            charts_data.append(data)
        self.context['charts_data'] = charts_data
        return render(request, 'index.html', self.context)

    def post(self, request):
        search = request.POST.get('search')
        if search:
            data = JsonToSQLModel.objects.filter(trade_code__icontains=search)
            self.context['all_data'] = data
        else:
            self.context['all_data'] = JsonToSQLModel.objects.all()
        trade_codes = list(JsonToSQLModel.objects.values_list('trade_code', flat=True).distinct())
        charts_data = []
        for trade_code in trade_codes:
            queryset = JsonToSQLModel.objects.filter(trade_code=trade_code)
            data = {
                'trade_code': trade_code,
                'dates': [entry.date.strftime('%y-%m-%d') for entry in queryset],
                'close_dates': [str(entry.close) for entry in queryset],
                'volume_dates': [entry.volume for entry in queryset],
            }
            charts_data.append(data)
        self.context['charts_data'] = charts_data
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
    
class DeleteView(View):
    def get(self, request, pk):
        JsonToSQLModel.objects.get(pk=pk).delete()
        return redirect('index')
        
        
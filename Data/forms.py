from .models import JsonToSQLModel
from django import forms   

class EditForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.SelectDateWidget(years=range(1900, 2023), 
        attrs={'style': 'width: 33%; display: inline-block;', 'class': 'form-control'}),
    )
    trade_code = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    high = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    low = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    open = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    close = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    volume = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    class Meta:
        model = JsonToSQLModel
        fields = '__all__'
        
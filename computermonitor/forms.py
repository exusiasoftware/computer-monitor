from django import forms
from .models import Computer

class ComputerForm(forms.ModelForm):
    class Meta():
      model = Computer
      fields = ('name','user','model','model_type','platform','serial_number','manufacturer','manufacturer_site','schedule_backup_day','schedule_backup_time','create_date')
      
      widgets = {

          'name':forms.TextInput(attrs={'class':'form-group'}),
          'user':forms.TextInput(attrs={'class':'form-group'}),
          'model':forms.TextInput(attrs={'class':'form-group'}),
          'model_type':forms.TextInput(attrs={'class':'form-group'}),
          'serial_number':forms.TextInput(attrs={'class':'form-group'}),
          'manufacturer':forms.TextInput(attrs={'class':'form-group'}),
          'manufacturer_site':forms.TextInput(attrs={'class':'form-group'}),
          'schedule_backup_time':forms.TextInput(attrs={'class':'form-group'}),
          'create_date':forms.TextInput(attrs={'class':'form-group'}),
      }




from django import forms
from .models import StudentInformation,Product 

# class StudentInformationForm(forms.Form):
#     first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     last_name = forms.CharField(max_length=100)
#     id = forms.IntegerField()
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Enter Your Email Address'}))
#     subject = forms.IntegerField()
#     message = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'rows': 7,'class':'form-control'}))
    
    
class StudentInformationForm(forms.ModelForm):
    class Meta:
        model = StudentInformation
        fields = ['first_name', 'last_name', 'st_id','email']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['image','title','color']

from django import forms
from .models import *

class form1(forms.ModelForm):
	firstname=forms.CharField(widget=forms.TextInput(attrs={'size':30,'placeholder':'Enter Your Name'}))
	middlename=forms.CharField(widget=forms.TextInput(attrs={'size':30,'placeholder':'Enter Your Name'}))
	lastname=forms.CharField(widget=forms.TextInput(attrs={'size':30,'placeholder':'Enter Your Name'}))
	public_key=forms.CharField(widget=forms.Textarea)
	password = forms.CharField(widget=forms.PasswordInput(attrs={'size':30,'placeholder':'Type your password'}))
	email=forms.EmailField(widget=forms.TextInput(attrs={'size':30,'placeholder':'Enter Email Address'}))
	class Meta:
		model = user
		fields = ('firstname','middlename','lastname','public_key', 'email','password',)

class meso1(forms.ModelForm):
	receiver=forms.ModelChoiceField(queryset=user.objects.all(),initial='')
	sender=forms.ModelChoiceField(queryset=user.objects.all(),initial='')
	Message=forms.CharField(widget=forms.Textarea)
	
	class Meta:
		model = Meso
		fields = ('receiver','Message','sender',)
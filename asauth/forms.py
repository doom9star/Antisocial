from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Name', 
	'class': 'px-4 py-2 mb-2 border outline-none w-96 text-xs', 'autofocus': 'True'}),max_length=100)
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 
	'class': 'px-4 py-2 mb-2 border outline-none w-96 text-xs'}), min_length=8)

class RegisterForm(forms.Form):
	username = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Name', 
	'class': 'px-4 py-2 mb-2 border outline-none w-96 text-xs', 'autofocus': 'True'}),max_length=100)
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 
	'class': 'px-4 py-2 mb-2 border outline-none w-96 text-xs'}), min_length=8)
	cpassword = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 
	'class': 'px-4 py-2 mb-2 border outline-none w-96 text-xs'}), min_length=8)
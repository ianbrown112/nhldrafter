from django import forms
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()

class RegisterForm(forms.ModelForm):

	password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('username', 'email',)

	def clean_email(self):
		email = self.cleaned_data.get("email")
		qs = User.objects.filter(email__iexact=email)
		if qs.exists():
			raise forms.ValidationError("Email is already registered.")
		return email

	def clean_password2(self):
		#Check that password entries match
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")

		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Your passwords do not match")
		return password2

	def save(self, commit=True):
		#Save the provided password in hash format
		user = super(RegisterForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		user.is_active = False
		#create a new user hash for activating email

		if commit:
			user.is_active = True
			user.save()

		return user
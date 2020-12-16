from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

class User_form(UserCreationForm):

	class Meta:

		model = User 
		fields = ["username", "password1", "password2", "email",
					"first_name", "last_name"]

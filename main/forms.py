from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class SignUpForm(UserCreationForm):
    ROLE_CHOICES = [('S', 'Seller'), ('B', 'Buyer')]
    role = forms.ChoiceField(
        label="Choose Your User Type",
        required=True,
        choices=ROLE_CHOICES
    )
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ['role', 'first_name', 'last_name', 'username', 'email', 'password1']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        
        profile = Profile.objects.create(
            user=user,
            role=self.cleaned_data["role"],
            first_name=self.cleaned_data["first_name"], 
            last_name=self.cleaned_data["last_name"],  
            email=self.cleaned_data["email"],
        )
        return user


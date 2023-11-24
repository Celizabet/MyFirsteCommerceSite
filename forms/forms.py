from django import forms
from datetime import date
from .models import UserClientModel

years_options = [x for x in range(1955,2010)]
gender_options = [
    ("f","FEMALE"),
    ("m","MALE"),
    ("rns","RATHER NOT SAYING") 
]

# Form de registro del Usuario - Cliente
class UserClientModelForm(forms.ModelForm):
    password_confirmation = forms.CharField(
        label="Password Confirm", 
        widget=forms.PasswordInput(attrs={"placeholder":"confirm your password"})
    )

    class Meta():
        model = UserClientModel
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",           
            "email",
            "password",            
            "birthdate",
            "gender",
            "phone_number"
        ]
        widgets = {
            "id": forms.HiddenInput(attrs={"placeholder":"ID"}),
            "username": forms.TextInput(attrs={"placeholder":"Username"}),
            "first_name": forms.TextInput(attrs={"placeholder":"First Name"}),
            "last_name": forms.TextInput(attrs={"placeholder":"Last Name"}),           
            "email": forms.TextInput(attrs={"placeholder":"Email"}),
            "password": forms.PasswordInput(attrs={"placeholder":"Password"}),           
            "birthdate": forms.SelectDateWidget(years=years_options),
            "gender": forms.Select(choices=gender_options),
            "phone_number": forms.TextInput(attrs={"placeholder":"Phone Number"})
        }

    def clean_username(self, *args, **kwargs): 
        username = self.cleaned_data.get("username")  
        if UserClientModel.objects.filter(username=username).exists():
            raise forms.ValidationError("The given username already exists")
        return username

    def clean_birthdate(self):
        birthdate = self.cleaned_data.get("birthdate")
        today = date.today()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        if age < 18:
            raise forms.ValidationError("You must be at least 18 years old to register")
        return birthdate

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if len(password) < 5 or len(password) > 10:
            raise forms.ValidationError("Password must be between 5 and 10 characters") 
        return password
        
    
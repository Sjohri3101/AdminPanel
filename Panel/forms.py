from django import forms
from Panel.models import Employee  # Make sure to import your Employee model
from datetime import date

SPECIAL_CHAR = set('!@#$%^&*()_+=-[]{}|;:"\',.<>?/`~')

class EmployeeForm(forms.ModelForm):
    first_name = forms.CharField(
        label="First Name",
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-sm',
            'placeholder': ' ',  # Placeholder must be a space for floating labels
            'id': 'floatingFirstName'
        }),
    )
    
    last_name = forms.CharField(
        label="Last Name",
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-sm',
            'placeholder': ' ',  # Placeholder must be a space
            'id': 'floatingLastName'
        }),
    )
    
    username = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control form-control-sm',
            'placeholder': ' ',  # Placeholder must be a space
            'id': 'floatingEmail'
        }),
    )
    
    phone_number = forms.CharField(
        label="Contact",
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-sm',
            'placeholder': ' ',  # Placeholder must be a space
            'id': 'floatingPhone'
        }),
    )
    
    # emp_code = forms.CharField(
    #     label="Employee Code",
    #     max_length=50,
    #     required=True,
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control form-control-sm',
    #         'placeholder': ' ',  # Placeholder must be a space
    #         'id': 'floatingEmpCode'
    #     }),
    # )
    
    password = forms.CharField(
        label="Password",
        max_length=50,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-sm',
            'placeholder': ' ',  # Placeholder must be a space
            'id': 'floatingPassword'
        }),
    )
    
    date_of_birth = forms.DateField(
        label="Date of Birth",
        required=True,
        widget=forms.DateInput(attrs={
            'class': 'form-control form-control-sm',
            'type': 'date',
            'id': 'floatingDOB'  # Ensure a unique ID
        }),
    )
    
    gender = forms.ChoiceField(
        label="Select Gender",
        required=True,
        choices=(
            ("", "-- Select --"),
            ("Male", 'Male'),
            ("Female", 'Female'),
            ("Transgender", 'Transgender'),
            ("Others", 'Others')
        ),
        widget=forms.Select(attrs={
            'class': 'form-select form-select-sm',
            'id': 'floatingGender'  # Ensure a unique ID
        }),
    )
    
    confirm_password = forms.CharField(
        label="Re-enter Password",
        max_length=30,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-sm',
            'placeholder': ' ',  # Placeholder must be a space
            'id': 'floatingConfirmPassword'
        }),
    )

    class Meta:
        model = Employee
        fields = [
            'username',
            'first_name',
            'last_name',
            'date_of_birth',
            'gender',
            'phone_number',
            'password'
        ]

    # def clean_first_name(self):
    #     fname = self.cleaned_data.get('first_name')
    #     if any(char in SPECIAL_CHAR for char in fname):
    #         raise forms.ValidationError('Special characters are not allowed in First Name')
    #     return fname

    # def clean_last_name(self):
    #     lname = self.cleaned_data.get('last_name')
    #     if any(char in SPECIAL_CHAR for char in lname):
    #         raise forms.ValidationError('Special characters are not allowed in Last Name')
    #     return lname
    
    # def clean_gender(self):
    #     gender = self.cleaned_data.get('gender')
    #     # valid_genders = ['Male', 'Female', 'Transgender', 'Others']
    #     if not gender:
    #         raise forms.ValidationError('No gender selected. Please choose a valid option.')
    #     return gender

    # def clean_date_of_birth(self):
    #     date_of_birth = self.cleaned_data.get('date_of_birth')
    #     if date_of_birth:
    #         today = date.today()
    #         if date_of_birth > today:
    #             raise forms.ValidationError('Date of birth cannot be in the future.')
    #     return date_of_birth

    # def clean_email(self):
    #     username = self.cleaned_data.get('username')
    #     if Employee.objects.filter(email__iexact=username).exists():
    #         raise forms.ValidationError("Email is already in use.")
    #     return username

    # def clean_password(self):
    #     password = self.cleaned_data.get('password')
    #     if not password:
    #         raise forms.ValidationError("This field is required.")
    #     if len(password) < 8:
    #         raise forms.ValidationError("Password must be at least 8 characters long.")
    #     if not any(char.isupper() for char in password):
    #         raise forms.ValidationError("Password must contain at least one uppercase letter.")
    #     if not any(char.islower() for char in password):
    #         raise forms.ValidationError("Password must contain at least one lowercase letter.")
    #     if not any(char.isdigit() for char in password):
    #         raise forms.ValidationError("Password must contain at least one digit.")
    #     special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
    #     if not any(char in special_characters for char in password):
    #         raise forms.ValidationError("Password must contain at least one special character.")
    #     return password

    # def clean_confirm_password(self):
    #     password = self.cleaned_data.get('password')
    #     confirm_password = self.cleaned_data.get('confirm_password')
    #     if password and confirm_password and password != confirm_password:
    #         raise forms.ValidationError("Passwords do not match.")
    #     return confirm_password

    # def clean_phone_number(self):
    #     phone = self.cleaned_data.get('phone_number')
    #     if len(phone) < 10:  # Assuming phone number must be at least 10 digits
    #         raise forms.ValidationError("Enter a valid phone number.")
    #     return phone


class LoginForm(forms.Form):
    username = forms.EmailField(
        label="Email",
        max_length=254,
        widget=forms.EmailInput(attrs={
            'class': 'form-control form-control-sm',
            'placeholder': 'Enter your email',
            'id': 'loginEmail'
        }),
        required=True
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-sm',
            'placeholder': 'Enter your password',
            'id': 'loginPassword'
        }),
        required=True
    )

    def clean_username(self):
        email = self.cleaned_data.get('username')
        if not email:
            raise forms.ValidationError("This field is required.")
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise forms.ValidationError("This field is required.")
        return password
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your email address'}))
    first_name = forms.ChoiceField(label='', max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your first name'}))
    last_name = forms.ChoiceField(label='', max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your first name'}))


    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].widget.attrs['placeholder']='Enter your username'
        self.fields['username'].label=''
        self.fields['username'].help_text='<span class="form-text text-muted small">Required. 150 characters or fewer</span>'

        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['placeholder']='Enter your password'
        self.fields['password1'].label=''
        self.fields['passwird1'].help_text='<span class="form-text text-muted small"><ul><li> Your password can\'t be too similar to your other personal information. </li> <li> YOur password contains at least 8 characters.</li><li> Your password can\'t be entirly numeric</li></ul></span>'


        self.fields['password2'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['placeholder']='Confirm your password'
        self.fields['password2'].label=''
        self.fields['passwird1'].help_text='<span class="form-text text-muted small"><ul><li> Enter the same password as before , for verification </li> <li> Your password can\'t be entirly numeric</li></ul></span>'


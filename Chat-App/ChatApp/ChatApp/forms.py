from django import forms
from django.utils.translation import gettext as _
from django.contrib.auth.hashers import make_password
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Fieldset


# class UserForm(forms.ModelForm):

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_id = 'id-UserForm'
#         self.helper.form_method = 'post'
#         self.helper.form_action='signup'
#         self.helper.add_input(Submit('submit', 'Sign up', css_class='btn-success'))

#         self.helper.layout = Layout(Fieldset('User informations', 'name', 'password', 
#                                               style="color: green;"),
#                                     Fieldset('Additional info', 'age',  
#                                               style="color: green;")
#                                     )

#     class Meta:
#         model = User
#         fields = ['name', 'password', 'age']
#         error_messages = {
#              'username':{
#                  'unique': _('Please enter another username. This one is already taken')
#              },
#          }
#         widgets = {
#             "name": forms.TextInput(attrs={'placeholder': 'Enter your nickname'}),
#             "password": forms.PasswordInput,
#         }

#     def save(self, commit=True, *args, **kwargs):
#         m = super().save(commit=False)
#         m.password = make_password(self.cleaned_data.get('password'))
#         m.username = self.cleaned_data.get('name').lower()

#         if commit:
#             m.save()
#         return m


# class LoginForm(forms.Form):
#     pass
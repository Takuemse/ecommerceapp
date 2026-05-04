from django import forms
from .models import Order
# ↑ import Django's form tools and our Order model


class OrderForm(forms.ModelForm):
    # ↑ ModelForm = a form that's connected to a database model
    # it automatically creates fields from the model

    class Meta:
        model = Order
        # ↑ this form is connected to the Order model
        
        fields = ['name', 'phone', 'address']
        # ↑ show only these three fields in the form

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter your full name'
            }),
            # ↑ attrs = extra HTML attributes added to the input box

            'phone': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter your phone number'
            }),

            'address': forms.Textarea(attrs={
                'class': 'form-input',
                'placeholder': 'Enter your delivery address',
                'rows': 4
                # ↑ rows=4 makes the text box taller
            }),
        }
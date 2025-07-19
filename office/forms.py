from django import forms

from office.models.lead_model import LeadModel

class LeadForm(forms.ModelForm):
    class Meta:
        model = LeadModel
        fields = [
            'contract',
            'name',
            'product',
            'adress',
            'phone',
            'email',
            'note',
        ]
        widgets = {
            'contact_date': forms.DateInput(attrs={'type': 'date'}),
            'note': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not phone.isdigit():
            raise forms.ValidationError("Телефон должен содержать только цифры")
        return phone

    def clean_email(self):
        email = self.cleaned_data['email']
        if '@' not in email:
            raise forms.ValidationError("Введите корректный email")
        return email
from django import forms

from company.models import CompanyModel
from office.models.lead_model import LeadModel
from office.models.order_model import OrderModel

from django.forms import DateInput, NumberInput, TextInput, CheckboxInput, Select, ValidationError
from datetime import date, timedelta, timezone


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
            'contract': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Автоматическая генерация'
            }),
            'name': TextInput(attrs={
                'class': 'form-control'
            }),
            'product': TextInput(attrs={
                'class': 'form-control'
            }),
            'adress': TextInput(attrs={
                'class': 'form-control'
            }),
            'phone': TextInput(attrs={
                'class': 'form-control',
            }),
            'email': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'example@domain.com'
            }),

        }

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not phone.isdigit():
            raise forms.ValidationError("Телефон должен содержать только цифры")
        return phone


class OrderForm(forms.ModelForm):

    company = forms.ModelChoiceField(
        queryset=CompanyModel.objects.filter(is_active=True),
        widget=forms.RadioSelect(attrs={'class': 'btn-check'}),
        empty_label=None
    )
    class Meta:
        model = OrderModel
        fields = '__all__'
        widgets = {
            'company': forms.RadioSelect(),
            'contract': TextInput(attrs={
                'class': 'form-control',
            }),
            'contract_date': DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'client_name': TextInput(attrs={
                'class': 'form-control'
            }),
            'delivery_address': TextInput(attrs={
                'class': 'form-control'
            }),
            'term': DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'add_date': DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'readonly': 'readonly'
            }),
            'product': TextInput(attrs={
                'class': 'form-control',
            }),
            'phone': TextInput(attrs={
                'class': 'form-control',
            }),
            'email': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'example@domain.com'
            }),
            'sum': NumberInput(attrs={
                'class': 'form-control'
            }),
            'prepayment': NumberInput(attrs={
                'class': 'form-control'
            }),
            'rebate': NumberInput(attrs={
                'class': 'form-control'
            }),
            'note': TextInput(attrs={
                'class': 'form-control'
            }),
            'sumdeliv': NumberInput(attrs={
                'class': 'form-control'
            }),
            'sumcollect': NumberInput(attrs={
                'class': 'form-control'
            }),
            'personal_agree': Select(attrs={
                'class': 'form-select'
            }),
            'rassr': CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'beznal': CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'archive': CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }

    def __init__(self, *args, **kwargs):
        lead_id = kwargs.pop('lead_id', None)
        super().__init__(*args, **kwargs)
        self.fields.pop('attention', 0)
        
        # Установка значений по умолчанию
        self.fields['add_date'].initial = date.today()
        self.fields['term'].initial = (date.today() + timedelta(weeks=4)).strftime('%Y-%m-%d')
        self.fields['personal_agree'].initial = False
        active_companies = CompanyModel.objects.filter(is_active=True)
        self.fields['company'].queryset = active_companies
        
        # Обработка привязки к лиду
        if lead_id:
            try:
                lead = LeadModel.objects.get(pk=lead_id)
                self.fields['contract'].initial = lead.contract
                self.fields['client_name'].initial = lead.name
                self.fields['product'].initial = lead.product
                self.fields['delivery_address'].initial = lead.adress
                self.fields['phone'].initial = lead.phone
                self.fields['email'].initial = lead.email
                self.fields['lead'].initial = lead.id
                self.fields['company'].initial = active_companies.first().id
                # Делаем поля из лида только для чтения
                self.fields['contract'].widget.attrs['readonly'] = True
            except LeadModel.DoesNotExist:
                pass
        else:
            # Если заказ создается без лида, разрешаем редактирование этих полей
            self.fields['contract'].widget.attrs.pop('readonly', None)

        # Настройка скрытых полей
        self.fields['lead'].widget = forms.HiddenInput()
        
        # Дополнительные настройки полей
        self.fields['email'].required = False
        self.fields['note'].required = False
        self.fields['personal_agree'].required = False
        self.fields['add_date'].required = False


    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not phone.isdigit():
            raise ValidationError("Телефон должен содержать только цифры")
        if len(phone) != 10:
            raise ValidationError("Телефон должен содержать 10 цифр")
        return phone

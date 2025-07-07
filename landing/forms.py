from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['full_name', 'phone', 'email', 'city']  # rõ ràng và bảo mật hơn '__all__'

        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Họ và tên của bạn'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Số điện thoại liên hệ'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Địa chỉ email'
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tỉnh/Thành phố sinh sống'
            }),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone.isdigit():
            raise forms.ValidationError("Số điện thoại chỉ được chứa chữ số.")
        if len(phone) < 9:
            raise forms.ValidationError("Số điện thoại quá ngắn.")
        return phone

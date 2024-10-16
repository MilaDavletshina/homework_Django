from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import Product


class ProductForm(forms.ModelForm):
    FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = ["name", "description", "image", "category", "price"]

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({'class': 'form-control','placeholder': 'Введите наименование продукта'})
        self.fields["description"].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите описание'})
        self.fields["image"].widget.attrs.update({'class': 'form-control', 'placeholder': 'Вставьте изображение'})
        self.fields["category"].widget.attrs.update({'class': 'form-control', 'placeholder': 'Укажите категорию'})
        self.fields["price"].widget.attrs.update({'class': 'form-control', 'placeholder': 'Укажите цену'})

    def clean_name(self):
        """ Валидация формы, на проверку отсутствия запрещенных слов в наименовании"""
        name = self.cleaned_data['name']
        for word in self.FORBIDDEN_WORDS:
            if word.lower() in name.lower():
                raise forms.ValidationError(f'Слово "{word}" запрещено в названии продукта')
        return name

    def clean_description(self):
        """ Валидация формы, на проверку отсутствия запрещенных слов в описании"""
        description = self.cleaned_data['description']
        for word in self.FORBIDDEN_WORDS:
            if word.lower() in description.lower():
                raise forms.ValidationError(f'Слово "{word}" запрещено в описании продукта')
        return description





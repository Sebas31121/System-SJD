from django import forms
from .models import Category, Product, Unity

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

    def __init__(self, *args, **kwargs) -> None:
        super(CategoryForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class UnityForm(forms.ModelForm):
    class Meta:
        model = Unity
        fields = ['name']

    def __init__(self, *arg, **kwargs) -> None:
        super(UnityForm, self).__init__(*arg, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control mt-1'})

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock', 'img_route', 'unity', 'category']

    def __init__(self, *args, **kwargs):
        self.is_edit = kwargs.pop('is_edit', False)
        super(ProductForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control mt-1'})
        
        if self.is_edit:
            self.fields['stock'].widget.attrs['readonly'] = 'readonly'
            self.fields['unity'].widget.attrs['disabled'] = 'disabled'
            self.fields['category'].widget.attrs['disabled'] = 'disabled'

    def clean(self):
        cleaned_data = super().clean()
        if self.is_edit:
            cleaned_data['stock'] = self.instance.stock
            cleaned_data['unity'] = self.instance.unity
            cleaned_data['category'] = self.instance.category
        return cleaned_data
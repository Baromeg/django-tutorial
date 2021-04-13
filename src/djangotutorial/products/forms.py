from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Your title'}))
    # email = forms.EmailField()
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={
        'class': 'new-class-name two',
        'id': 'my-id',
        'rows': 20,
        'cols': 120,
        'placeholder': 'Your description'
    }))
    price = forms.DecimalField(initial=199.99)

    class Meta:
        model = Product
        fields = {
            'title',
            'description',
            'price'
        }

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        # if not 'CFE' in title:
        #     raise forms.ValidationError('this is not a valid title')
        if not 'news' in title:
            raise forms.ValidationError('this is not a valid title')
        else:
            return title

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if not email.endswith('edu'):
            raise forms.ValidationError('this is not a valid email')
        else:
            return email


class RawProductForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Your title'}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={
        'class': 'new-class-name two',
        'id': 'my-id',
        'rows': 20,
        'cols': 120,
        'placeholder': 'Your description'
    }))
    price = forms.DecimalField(initial=199.99)

    class Meta:
        model = Product
        fields = {
            'title',
            'description',
            'price'
        }

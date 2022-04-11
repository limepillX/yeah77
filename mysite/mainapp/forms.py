from django import forms


class AddDataForm(forms.Form):
    data = forms.CharField(widget=forms.TextInput(attrs={'style': "font-size: 25px"}), label='', label_suffix='')

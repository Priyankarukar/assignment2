from django import forms

class MyForm(forms.Form):
    Height=forms.CharField(label="Height",max_length=100)
    weight=forms.CharField(label="Weight",max_length=100)

from django import forms


class PathForm(forms.Form):
    path = forms.CharField(label="Путь к папке", max_length=255)

from django import forms


class UserForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    surname = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    patronymic = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    faculty = forms.ChoiceField(choices=[
        ("Физико-математический", "Физико-математический"),
        ("Филологический", "Филологический"),
        ("Экономики и управления", "Экономики и управления"),
        ("Социологический", "Социологический"),
        ("Психолого-педагогический", "Психолого-педагогический"),
        ("Истории и права", "Истории и права"),
        ("Искусства и дизайна", "Искусства и дизайна"),
        ("Естественно-географический", "Естественно-географический")
    ], widget=forms.Select(attrs={"class": "form-select"}))
    age = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    agreement = forms.BooleanField(widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))

from django.forms import (Form, EmailField, CharField, PasswordInput, BooleanField, RegexField, ChoiceField,
                          IntegerField)

class RegistrationForm(Form):
    name = RegexField(max_length=15, min_length=2, label='Имя:', regex='')
    surname = RegexField(max_length=30, min_length=2, label='Фамилия:', regex='')
    email = EmailField(label='Электронная почта:')
    username = CharField(min_length=6, label='Логин пользователя')
    password = CharField(widget=PasswordInput)
    confirmation_password = CharField(widget=PasswordInput)
    age = IntegerField(max_value=100, label='Возраст:', required=True)
    gender = ChoiceField(choices=[('men', 'Men'), ('female', 'Female')], label='Пол')
    checkbox_accept_rules = BooleanField(required=True, label='Согласие c правилами')

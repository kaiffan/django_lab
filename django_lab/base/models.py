from typing import Any
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from django.db import models


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.CharField(max_length=255, unique=True)
    login = models.CharField(max_length=255)
    password_hash = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=255)
    date_registration = models.DateTimeField(default=datetime.utcnow)
    user_theme = models.CharField()


    def get_hash_password(self, password: str) -> str:
        return generate_password_hash(
            password=password
        )


    def check_password(self, password_check: str) -> bool:
        return check_password_hash(
            pwhash=self.password_hash,
            password=password_check
        )

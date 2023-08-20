from django.db import models
from django.contrib.auth.models import User


class MarkaVehicle(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class MarkaModel(models.Model):
    name = models.ForeignKey(MarkaVehicle, on_delete=models.SET_NULL, null=True)
    model = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} {self.model}'


class Ad(models.Model):
    TYPES_VEHICLE = (
        ('легковой', ' Легковой'),
        ('коммерческий', 'Грузовой'),
        ('мотоцикл', 'Мотоцикл'),
    )
    TYPES_RUDDER = (
        ('левый', 'Левый'),
        ('правый', 'Правый')
    )
    TYPES_AD = (
        ('обычное', 'Обычное'),
        ('вип', 'Вип'),
        ('ремиум', 'Премиум')
    )
    TYPES_TRANSMISSION = (
        ('передний', 'Передний'),
        ('задний', 'Задний'),
        ('олный', 'Полный')
    )
    TYPES_BODY = (
        ('седан', 'Седан'),
        ('хетчбек', 'Хетчбек'),
        ('купе', 'Купе'),
        ('внедорожник', 'Внедорожник'),
        ('пикап', 'Пикап'),
        ('универсал', 'Универсал'),
        ('лифтбек', 'Лифтбек'),
        ('кабриолет', 'Кабриолет'),
        ('минивен', 'Минивен')
    )
    TYPES_ENGINE = (
        ('дизель', 'Дизель'),
        ('бензин', 'Бензин'),
        ('электро', ' Электро'),
        ('гибрид', 'Гибрид'),
        ('газ', 'Газ')
    )
    TYPES_DRIVE = (
        ('механическая', 'Механическая'),
        ('робот', 'Робот'),
        ('автоматическая', 'Автоматическая')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    marka = models.ForeignKey(MarkaVehicle, models.CASCADE)
    type_rudder = models.CharField(choices=TYPES_RUDDER, max_length=20)
    type_vehicle = models.CharField(choices=TYPES_VEHICLE, max_length=30)
    type_transmission = models.CharField(choices=TYPES_TRANSMISSION, max_length=20)
    type_drive = models.CharField(choices=TYPES_DRIVE, max_length=20)
    type_body = models.CharField(choices=TYPES_BODY, max_length=20)
    type_engine = models.CharField(choices=TYPES_ENGINE, max_length=20)
    date = models.DateField()
    type_ad = models.CharField(choices=TYPES_AD, max_length=20)

    def __str__(self):
        return f'{self.user} {self.marka} {self.date}'

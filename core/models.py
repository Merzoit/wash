from django.db import models

# Create your models here.
class Blank(models.Model):
    """Модель для создания объекта мойки"""
    #Related fields
    date = models.ForeignKey(
        'Date', db_column='date', on_delete=models.SET_NULL,
        blank=True, null=True, verbose_name="Дата",
        )
    car_class = models.ForeignKey(
        'Car_class', db_column='car_class', on_delete=models.SET_NULL, 
        blank=True, null=True, verbose_name="Класс авто"
        )
    wash_type = models.ForeignKey(
        'Wash_type', db_column='wash_type', on_delete=models.SET_NULL, 
        blank=True, null=True, verbose_name="Тип мойки"
        )
    wash_man = models.ForeignKey(
        'Wash_man', db_column='wash_man', on_delete=models.SET_NULL,
        blank=True, null=True, verbose_name="Мойщик"
        )
    pay_type = models.ForeignKey(
        'Pay', db_column='pay', on_delete=models.SET_NULL,
        blank=True, null=True, verbose_name="Способ оплаты"
        )
    service = models.ManyToManyField('Service', verbose_name="Услуги") 
    #Local fields
    time = models.TimeField(auto_now=True)
    grz = models.CharField(max_length=9, blank=True, null=True, verbose_name="ГРЗ автомобиля")
    car_mark = models.CharField(max_length=32, blank=True, null=True, verbose_name="Марка автомобиля")
    price = models.IntegerField(blank=True, null=True, verbose_name="Цена")        
    notes = models.TextField(max_length=360, blank=True, null=True, verbose_name="Примечания")
    sale = models.IntegerField(default=0, verbose_name="Скидка")
    super_clean = models.BooleanField(default=False, verbose_name="Химчистка")
    night_clean = models.BooleanField(default=False, verbose_name="Ночная")
    done_clean = models.BooleanField(default=False, verbose_name="Готова")
    class Meta:
        """ Конфигурация класса """
        verbose_name = "Бланк"
        verbose_name_plural = "Бланки"


class Date(models.Model):
    """Модель для смен"""
    date = models.DateField(verbose_name="Дата", unique=True)

    def __str__(self):
        """ UI админки """
        return str(self.date)

    class Meta:
        """ Конфигурация класса """
        verbose_name = "Дата"
        verbose_name_plural = "Даты"
        ordering = ('-id',)


class Wash_type(models.Model):
    """Модель для типов мойки"""
    type = models.CharField(max_length=32, blank=True, null=True, verbose_name="Тип")

    def __str__(self):
        """ UI админки """
        return self.type

    class Meta:
        """ Конфигурация класса """
        verbose_name = "Тип мойки"
        verbose_name_plural = "Типы мойки"


class Wash_man(models.Model):
    """Модель для мойщиков"""
    man = models.CharField(max_length=32, blank=True, null=True, verbose_name="Мойщик")

    def __str__(self):
        """ UI админки """
        return self.man

    class Meta:
        """ Конфигурация класса """
        verbose_name = "Мойщик"
        verbose_name_plural = "Мойщики"


class Car_class(models.Model):
    """Модель для классов авто"""
    car_class = models.CharField(max_length=16, blank=True, null=True, verbose_name="Тип")

    def __str__(self):
        """ UI админки """
        return self.car_class

    class Meta:
        """ Конфигурация класса """
        verbose_name = "Класс авто"
        verbose_name_plural = "Классы авто"


class Pay(models.Model):
    """Модель для оплаты"""
    pay_type = models.CharField(max_length=8, null=True, blank=True, verbose_name="Оплата")

    def __str__(self):
        """ UI админки """
        return self.pay_type

    class Meta:
        """ Конфигурация класса """
        verbose_name = "Способ оплаты"
        verbose_name_plural = "Способы оплаты"


class Service(models.Model):
    """Модель для услуг"""
    service = models.CharField(max_length=24, blank=True, null=True, verbose_name="Услуга")

    def __str__(self):
        """ UI админки """
        return self.service

    class Meta:
        """ Конфигурация класса """
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
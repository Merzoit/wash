from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import *
from .forms import AddBlankForm, LoginUserForm, AddDate

class ManDate:
    """Запрос для фильтра"""
    def get_washman(self):
        """Все мойщики"""
        return Wash_man.objects.all()

    def get_date(self):
        """Все смены"""
        return Date.objects.all().order_by("-id")


class LoginView(LoginView):
    """Вход"""
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    template_name = 'login.html'
    form_class = LoginUserForm
    success_url = reverse_lazy('monitor_blank')
    def get_success_url(self):
        return self.success_url


class LogoutView(LogoutView):
    """Выход"""
    next_page = reverse_lazy('login')


class CreateBlankView(LoginRequiredMixin, ManDate, CreateView):
    """Добавление бланка в бвзу моек"""
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    template_name = 'add_blank.html'
    form_class = AddBlankForm
    success_url = reverse_lazy('add_blank')    
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class ListBlankView(LoginRequiredMixin, ManDate, ListView):
    """Список моек"""
    model = Blank
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    def get_context_data(self, **kwargs):
        kwargs['blank_list'] = Blank.objects.all()
        return super().get_context_data(**kwargs)


class FilterView(ManDate, ListView):
    """"""
    model = Blank
    def get_context_data(self, **kwargs):
        """Контекст для фильтра зарплат"""
        queryset = Blank.objects.filter(
            Q(date__in=self.request.GET.getlist("date")) ,
            Q(wash_man__in=self.request.GET.getlist("man"))
        )
        wash_count = len(queryset)

        def full_money():
            """Общая прибыль"""
            result = 0
            for i in queryset:
                result += i.price
            return result

        def get_money():
            """Зарплата мойщика"""
            result = 0
            for i in queryset:
                if i.super_clean:
                    #При химчистке
                    result += i.price * 0.5
                else:
                    #Без химчистки
                    result += i.price * 0.3
            return result

        def clean_count():
            """Счётчик химчистки"""
            result = 0
            for i in queryset:
                if i.super_clean:
                    result += 1
            return result

        kwargs['api'] = {
            'wash_count': wash_count,
            'full_money': full_money(),
            'get_money': get_money(),
            'clean_count': clean_count(),
            'blank_list': queryset
        }
        return super().get_context_data(**kwargs)


class BlankMonitoringView(LoginRequiredMixin, ManDate, CreateView):
    """ Управление мойкой """
    model = Date
    fields = '__all__'
    template_name = 'core/monitor_blank.html'
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        """Передаю контекст"""
        q = Date.objects.first()
        list = Blank.objects.filter(date=q).order_by("-id")

        def admin_money_full():
            """Сумма для зарплаты администратора"""
            bank = 0
            for i in list:
                if not i.night_clean:
                    bank += i.price
            return bank

        def admin_money():
            """Зарплата администратора"""
            if admin_money_full() <= 20000:
                return 2000
            else:
                return admin_money_full * 0.1

        def wash_money():
            """Прибыль мойки"""
            result = 0
            for i in list:
                result += i.price + i.price * i.sale * 0.01
            return result
        
        def not_ready_counter():
            """Счётчик моек в работе"""
            result = 0
            for i in list:
                if not i.done_clean:
                    result += 1
            return result

        kwargs["api"] = {
            'list': list,
            'not_ready_counter': not_ready_counter(),
            'wash_counter': len(list),
            'success_date': q,
            'wash_money': wash_money(),
            'admin_money_full': admin_money_full(),
            'admin_money': admin_money(),
            }
        return super().get_context_data(**kwargs)
    
    
class BlankUpdateView(UpdateView):
    """Редактирование моек"""
    model = Blank
    template_name = 'blank_update.html'
    form_class = AddBlankForm
    success_url = reverse_lazy('monitor_blank')
    #success_msg = 'Запись обновлена'
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class BlankDeleteView(DeleteView):
    """Удаление мойки"""
    model = Blank
    template_name = "delete_blank.html"
    success_url = reverse_lazy('monitor_blank')
    success_msg = "Мойка удалена"
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

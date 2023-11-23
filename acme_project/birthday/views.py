from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import BirthdayForm
from .models import Birthday
from .utils import calculate_birthday_countdown


class BirthdayMixin:
    model = Birthday
    form_class = BirthdayForm
    template_name = 'birthday/birthday.html'
    success_url = reverse_lazy('birthday:list')


class BirthdayListView(ListView):
    # Указываем модель, с которой работает CBV...
    model = Birthday
    # ...сортировку, которая будет применена при выводе списка объектов:
    ordering = 'id'
    # ...и даже настройки пагинации:
    paginate_by = 10
    # template_name = 'birthday/birthday_list.html'


class BirthdayCreateView(BirthdayMixin, CreateView):
    pass
    # Указываем модель, с которой работает CBV...
    # model = Birthday
    # Этот класс сам может создать форму на основе модели!
    # Нет необходимости отдельно создавать форму через ModelForm.
    # Указываем поля, которые должны быть в форме:
    # fields = '__all__'
    # ^^^^^^^^^^^^^^^^^^
    # Указываем имя формы:
    # form_class = BirthdayForm
    #
    # Явным образом указываем шаблон:
    # template_name = 'birthday/birthday.html'
    # Указываем namespace:name страницы, куда будет перенаправлен пользователь
    # после создания объекта:
    # success_url = reverse_lazy('birthday:list')


class BirthdayUpdateView(BirthdayMixin, UpdateView):
    pass
    # model = Birthday
    # form_class = BirthdayForm
    # template_name = 'birthday/birthday.html'
    # success_url = reverse_lazy('birthday:list')


class BirthdayDeleteView(DeleteView):
    model = Birthday
    template_name = 'birthday/birthday_confirm_delete.html'
    success_url = reverse_lazy('birthday:list')

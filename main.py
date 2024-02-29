import tkinter as tk

from window import MainWindow
from button_length import ButtonWindow


class EEEConverter:
    # Класс управления ресурсами и поведением приложения

    def __init__(self):
        # Создание графического интерфейса
        self.screen = tk.Tk()
        self.screen.title('ЕЕЕКонвертер')

        # Создание объекта главного экрана
        self.main_window = MainWindow()

        # Создание объекта для величин длины
        self.length_values = ['Миллиметр', 'Сантиметр', 'Дециметр', 'Метр', 'Километр', 'Фут', 'Ярд', 'Дюйм', 'Миля',
                              'Морская миля']
        self.length_si = {'Миллиметр': 0.001,
                          'Сантиметр': 0.01,
                          'Дециметр': 0.1,
                          'Метр': 1,
                          'Километр': 1000,
                          'Фут': 0.348,
                          'Ярд': 0.9144,
                          'Дюйм': 0.00254,
                          'Миля': 1609.344,
                          'Морская миля': 1852}
        self.length_window = ButtonWindow(self.main_window.main_frm, self.length_values, self.length_si)

        # Создание объекта для кнопки величин массы
        self.weight_values = ['Миллиграмм', 'Грамм', 'Килограмм', 'Центнер', 'Тонн', 'Пуд', 'Фунт', 'Карат', 'Унция']
        self.weight_si = {'Пуд': 16.38,
                          'Килограмм': 1,
                          'Миллиграмм': 0.000001,
                          'Грамм': 0.001,
                          'Фунт': 0.45,
                          'Тонн': 1000,
                          'Центнер': 100,
                          'Карат': 0.0002,
                          'Унция': 0.028}
        self.weight_window = ButtonWindow(self.main_window.main_frm, self.weight_values, self.weight_si)

        # Создание объекта для кнопки величин объема
        self.volume_values = ['Миллилитр', 'Литр', 'Кубический миллиметр', 'Кубический дециметр',
                              'Кубический сантиметр',
                              'Кубический метр', 'Кварта', 'Пинта', 'Галлон', 'Унция', 'Кубический фут',
                              'Кубический дюйм']
        self.volume_si = {'Литр': 1,
                          'Миллилитр': 0.001,
                          'Кубический метр': 1000,
                          'Кубический дециметр': 1,
                          'Кубический сантиметр': 0.001,
                          'Кубический миллиметр': 0.000001,
                          'Кварта': 1.1365,
                          'Пинта': 0.5682,
                          'Галлон': 4.5461,
                          'Унция': 0.0296,
                          'Кубический фут': 28.3168,
                          'Кубический дюйм': 0.0164}
        self.size_window = ButtonWindow(self.main_window.main_frm, self.volume_values, self.volume_si)

        # Назначение команды для кнопок главного экрана
        self.main_window.btn_lenght['command'] = self.length_window.run_window
        self.main_window.btn_weight['command'] = self.weight_window.run_window
        self.main_window.btn_volume['command'] = self.size_window.run_window

        # Назначение команды для кнопки возврата
        self.length_window.reverse_btn['command'] = self.run_screen
        self.weight_window.reverse_btn['command'] = self.run_screen
        self.size_window.reverse_btn['command'] = self.run_screen

    def run_screen(self):
        # Функция запуска главного экрана

        # Очистка предыдущих окон
        self.length_window.button_frm.pack_forget()
        self.weight_window.button_frm.pack_forget()
        self.size_window.button_frm.pack_forget()

        # Запуск главного окна
        self.main_window.run_window()
        self.screen.mainloop()


if __name__ == '__main__':
    ec = EEEConverter()
    ec.run_screen()

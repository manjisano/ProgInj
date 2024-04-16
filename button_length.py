import tkinter as tk
from tkinter import ttk


class ButtonWindow:

    def __init__(self, main_window, values, si_values):
        # Функция для интерфейса для конвертера длин
        # Очистка главного окна и создания нового
        self.screen = main_window
        self.button_frm = tk.Frame(
            relief='flat',
            bg='white'
        )
        # Определение словаря для перевода значений
        self.si = si_values

        # Создание комбобоксов
        combobox_values = values
        combobox_var_in = tk.StringVar(value=combobox_values[0])
        combobox_var_out = tk.StringVar(value=combobox_values[0])
        self.combobox_input = tk.ttk.Combobox(
            master=self.button_frm,
            width=28,
            height=20,
            font='Georgia 14',
            textvariable=combobox_var_in,
            values=combobox_values,
            state='readonly'
        )

        self.combobox_print = tk.ttk.Combobox(
            master=self.button_frm,
            width=28,
            height=20,
            font='Georgia 14',
            textvariable=combobox_var_out,
            values=combobox_values,
            state='readonly'
        )

        # Создание других виджетов
        self.insert_ent = tk.Entry(
            master=self.button_frm,
            width=25,
            text='Введите число',
            fg='black',
            bg="grey",
            font='Georgia 18',
            justify='center'
        )

        self.buttons_frm = tk.Frame(
            master=self.button_frm,
            relief='flat',
            bg='white'
        )

        self.convert_btn = tk.Button(
            master=self.buttons_frm,
            text='\N{RIGHTWARDS BLACK ARROW}',
            command=self.lenght_convert,
            font='Georgia 14'
        )

        self.reverse_btn = tk.Button(
            master=self.buttons_frm,
            text='\N{ANTICLOCKWISE TOP SEMICIRCLE ARROW}',
            font='Georgia 14'
        )

        self.clean_btn = tk.Button(
            master=self.buttons_frm,
            text='\N{Black Universal Recycling Symbol}',
            command=self.clear_text,
            font='Georgia 14'
        )

        self.lbl_result = tk.Label(
            master=self.button_frm,
            width=32,
            bg="grey",
            borderwidth='2',
            font='Georgia 14'
        )

    def lenght_convert(self):
        # Процеура для расчета величин
        # Принимает значения из комбобокса
        selection_input = self.combobox_input.get()
        selection_print = self.combobox_print.get()
        # Проверка на правильность ввода и формула для перевода
        try:
            if float(self.insert_ent.get()) < 999999 and float(self.insert_ent.get()) > 0.00009:
                # Расчет результата
                result = float(self.insert_ent.get()) * self.si[selection_input] / self.si[selection_print]
                if result > 0.00009 and result < 999999:
                    # Вывод получившгося значения
                    self.lbl_result['text'] = f'{result}'
                else:
                    # Вывод при слишком малом или большом введенном значении
                    self.lbl_result['text'] = 'Число слишком мало или велико для вывода'
            else:
                # Вывод при слишком большом или малом введенном значении
                self.lbl_result['text'] = 'Вводимое число слишком велико или мало'
        except ValueError:
            # Вывод при ошибки несоответсвия типов
            self.lbl_result['text'] = 'Введенно неверное значение'

    def run_window(self):
        self.screen.pack_forget()
        # Вывод интерфейса
        self.button_frm.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.insert_ent.pack(ipady=10)
        self.combobox_input.pack()

        self.buttons_frm.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.convert_btn.grid(row=0, column=1, padx=40, pady=10)
        self.reverse_btn.grid(row=0, column=0, padx=50, pady=10)
        self.clean_btn.grid(row=0, column=2, padx=40, pady=10)

        self.combobox_print.pack()
        self.lbl_result.pack(ipady=10)


    def clear_text(self):
        # Процедура очистки виджетов

        self.insert_ent.delete(0, 'end')
        self.lbl_result['text'] = ''
        self.combobox_print.set('')
        self.combobox_input.set('')

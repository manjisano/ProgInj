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
            width=10,
            font='Arial',
            textvariable=combobox_var_in,
            values=combobox_values,
            state='readonly'
        )

        self.combobox_print = tk.ttk.Combobox(
            master=self.button_frm,
            width=10,
            font='Arial',
            textvariable=combobox_var_out,
            values=combobox_values,
            state='readonly'
        )

        # Создание других виджетов
        self.insert_ent = tk.Entry(
            master=self.button_frm,
            width=15,
            fg='white',
            bg="black",
            font='Arial'
        )

        self.buttons_frm = tk.Frame(
            master=self.button_frm,
            relief='flat',
            bg='white'
        )

        self.convert_btn = tk.Button(
            master=self.buttons_frm,
            text='\N{RIGHTWARDS BLACK ARROW}',
            command=self.lenght_convert
        )

        self.reverse_btn = tk.Button(
            master=self.buttons_frm,
            text='\N{ANTICLOCKWISE TOP SEMICIRCLE ARROW}',
        )

        self.clean_btn = tk.Button(
            master=self.buttons_frm,
            text='\N{Black Universal Recycling Symbol}',
            command=self.clear_text
        )

        self.lbl_result = tk.Label(
            master=self.button_frm,
            width=12,
            fg='white',
            bg='black',
            font='Arial'
        )

    def lenght_convert(self):
        # Функция для расчета величин
        selection_input = self.combobox_input.get()
        selection_print = self.combobox_print.get()

        # Проверка на правильность ввода и формула для перевода
        try:
            self.lbl_result['text'] = '%.4f' % (
                        float(self.insert_ent.get()) * self.si[selection_input] / self.si[selection_print])
        except ValueError :
            self.lbl_result['text'] = 'Введенно неверное значение'

    def run_window(self):
        self.screen.pack_forget()
        # Вывод интерфейса
        self.button_frm.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.insert_ent.pack()
        self.combobox_input.pack()

        self.buttons_frm.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.convert_btn.grid(row=0, column=1, padx=10, pady=5)
        self.reverse_btn.grid(row=0, column=0, padx=10, pady=5)
        self.clean_btn.grid(row=0, column=2, padx=10, pady=5)

        self.lbl_result.pack()
        self.combobox_print.pack()

    def clear_text(self):

        self.insert_ent.delete(0, 'end')
        self.lbl_result['text'] = ''
        self.combobox_print.set('')
        self.combobox_input.set('')

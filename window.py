import tkinter as tk


class MainWindow:

    def __init__(self):
        # Иницилизация виджетов
        self.main_frm = tk.Frame(
            relief='flat',
            bg='black'
        )

        self.lbl = tk.Label(
            master=self.main_frm,
            text='Выберите величину',
            font='Georgia 24',
            fg='white',
            bg='black'

        )

        self.btn_lenght = tk.Button(
            master=self.main_frm,
            text='Длина',
            font='Georgia 24',
            width=20,
            height=5,
            bg='white',
            fg='black'
        )

        self.btn_weight = tk.Button(
            master=self.main_frm,
            text='Масса',
            font='Georgia 24',
            width=20,
            height=5,
            bg='white',
            fg='black'
        )

        self.btn_volume = tk.Button(
            master=self.main_frm,
            text='Объём',
            font='Georgia 24',
            width=20,
            height=5,
            bg='white',
            fg='black'
        )

    def run_window(self):
        # Запуск основного окна
        self.main_frm.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.lbl.grid(row=0, column=1)
        self.btn_lenght.grid(row=1, column=0, padx=5, pady=5)
        self.btn_weight.grid(row=1, column=1, padx=5, pady=5)
        self.btn_volume.grid(row=1, column=2, padx=5, pady=5)

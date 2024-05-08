import unittest
import tkinter as tk
from tkinter import ttk


from button_length import ButtonWindow

class TestButtonWindow(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.values = ['Миллиметр', 'Сантиметр', 'Дециметр', 'Метр', 'Километр', 'Фут', 'Ярд', 'Дюйм', 'Миля',
                              'Морская миля']
        self.si_values = {'Миллиметр': 0.001,
                          'Сантиметр': 0.01,
                          'Дециметр': 0.1,
                          'Метр': 1,
                          'Километр': 1000,
                          'Фут': 0.348,
                          'Ярд': 0.9144,
                          'Дюйм': 0.00254,
                          'Миля': 1609.344,
                          'Морская миля': 1852}
        self.app = ButtonWindow(self.root, self.values, self.si_values)

    def tearDown(self):
        self.root.destroy()

    def test_valid_values(self):
        # Тест конвертации значений
        self.app.insert_ent.insert(0, '10')  # Вставляем значение
        self.app.combobox_input.set('Метр')
        self.app.combobox_print.set('Километр')
        self.app.convert()
        self.assertEqual(self.app.lbl_result['text'], '0.01')

    def test_input_values_out_of_range(self):
        self.app.insert_ent.insert(0, '1000000')  # Вставляем значение
        self.app.combobox_input.set('Километр')
        self.app.combobox_print.set('Миллиметр')
        self.app.convert()
        self.assertEqual(self.app.lbl_result['text'], 'Вводимое число слишком велико или мало')

        self.app.insert_ent.insert(0, '0.00001')  # Вставляем значение
        self.app.combobox_input.set('Метр')
        self.app.combobox_print.set('Километр')
        self.app.convert()
        self.assertEqual(self.app.lbl_result['text'], 'Вводимое число слишком велико или мало')

    def test_output_values_out_of_range(self):
        self.app.insert_ent.insert(0, '1000')  # Вставляем значение
        self.app.combobox_input.set('Морская миля')
        self.app.combobox_print.set('Миллиметр')
        self.app.convert()
        self.assertEqual(self.app.lbl_result['text'], 'Число слишком мало или велико для вывода')

        self.app.insert_ent.insert(0, '0.1')  # Вставляем значение
        self.app.combobox_input.set('Миллиметр')
        self.app.combobox_print.set('Морская миля')
        self.app.convert()
        self.assertEqual(self.app.lbl_result['text'], 'Число слишком мало или велико для вывода')

    def test_invalid_input(self):
        # Тестирование неправильных входных данных
        self.app.insert_ent.insert(0, 'abc')  # Вставляем неправильное значение
        self.app.combobox_input.set('Метр')
        self.app.combobox_print.set('Километр')
        self.app.convert()
        self.assertEqual(self.app.lbl_result['text'], 'Введенно неверное значение')


if __name__ == '__main__':
    unittest.main()
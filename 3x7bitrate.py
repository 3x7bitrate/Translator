import tkinter as tk

def convert_text():
    """Функция для выполнения конвертации текста."""
    text = input_text.get()  # Получаем текст из входного поля
    decimal_text = text_to_decimal(text)  # Выполняем конвертацию текста в десятичный код
    output_text.delete('1.0', tk.END)  # Очищаем выходное поле
    output_text.insert(tk.END, decimal_text)  # Вставляем результат в выходное поле

def text_to_decimal(text):
    """Функция для перевода текста в десятичный код."""
    decimal = ""
    for char in text:
        decimal += str(ord(char)) + " "  # Используем функцию ord() для получения кода символа
    return decimal

# Создаем окно приложения
root = tk.Tk()
root.title("Текст в Десятичный Код")

# Создаем входное поле
input_text = tk.Entry(root)
input_text.pack(pady=10)

# Создаем кнопку "Конвертировать"
convert_button = tk.Button(root, text="Конвертировать", command=convert_text)
convert_button.pack()

# Создаем выходное поле
output_text = tk.Text(root, height=10, width=30)
output_text.pack(pady=10)

# Запускаем цикл обработки событий Tkinter
root.mainloop()

"""
ord() - встроенная в Python функция. Принимает только один 
символ(иначе возникнет ошибка) и возвращает целое число - номер из 
таблицы символов Unicode, представляющий позицию данного символа.\
"""
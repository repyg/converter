import tkinter as tk
from tkinter import ttk, messagebox
from .api import fetch_exchange_rates
from .converter import convert_currency

class CurrencyConverterUI:
    def __init__(self):
        # Инициализация главного окна
        self.root = tk.Tk()
        self.root.title("Конвертер Валют")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        self.root.configure(bg="#f5f5f5")
        self.create_styles()
        self.create_widgets()

    def create_styles(self):
        """
        Создание пользовательских стилей для элементов интерфейса с использованием ttk.Style.
        """
        style = ttk.Style(self.root)
        style.theme_use("clam")
        style.configure("TLabel", background="#f5f5f5", font=("Helvetica", 12))
        style.configure("TButton", font=("Helvetica", 12), padding=8, relief="raised", background="#4caf50", foreground="white")
        style.configure("TCombobox", font=("Helvetica", 12), padding=5)
        style.map(
            "TButton",
            background=[("active", "#388e3c")],
            foreground=[("active", "white")],
        )

    def create_widgets(self):
        """
        Создание и расположение виджетов в главном окне.
        """
        # Заголовок
        title_frame = tk.Frame(self.root, bg="#4caf50", pady=10)
        title_frame.pack(fill=tk.X)
        title_label = tk.Label(
            title_frame, text="Конвертер Валют", font=("Helvetica", 20, "bold"), fg="white", bg="#4caf50"
        )
        title_label.pack()

        # Секция ввода данных
        input_frame = tk.Frame(self.root, bg="#f5f5f5", pady=20)
        input_frame.pack(fill=tk.BOTH, expand=True)

        # Базовая валюта
        tk.Label(input_frame, text="Выберите базовую валюту:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.base_currency_entry = ttk.Combobox(input_frame, values=self.get_currency_list())
        self.base_currency_entry.grid(row=0, column=1, padx=10, pady=5)
        self.base_currency_entry.set("USD")

        # Целевая валюта
        tk.Label(input_frame, text="Выберите целевую валюту:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.target_currency_entry = ttk.Combobox(input_frame, values=self.get_currency_list())
        self.target_currency_entry.grid(row=1, column=1, padx=10, pady=5)
        self.target_currency_entry.set("EUR")

        # Ввод суммы
        tk.Label(input_frame, text="Введите сумму:").grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.amount_entry = ttk.Entry(input_frame)
        self.amount_entry.grid(row=2, column=1, padx=10, pady=5)

        # Кнопка "Конвертировать"
        convert_button = ttk.Button(input_frame, text="Конвертировать", command=self.on_convert)
        convert_button.grid(row=3, column=0, columnspan=2, pady=20)

        # Результат
        self.result_label = tk.Label(input_frame, text="", font=("Helvetica", 14, "bold"), fg="#388e3c", bg="#f5f5f5")
        self.result_label.grid(row=4, column=0, columnspan=2, pady=10)

    def get_currency_list(self):
        """
        Возвращает список поддерживаемых валют.
        """
        return ["USD", "EUR", "JPY", "GBP", "AUD", "CAD", "CHF", "CNY", "NZD"]

    def on_convert(self):
        """
        Обрабатывает конвертацию валют при нажатии на кнопку "Конвертировать".
        """
        base_currency = self.base_currency_entry.get().upper()
        target_currency = self.target_currency_entry.get().upper()

        try:
            # Проверка введённой суммы
            amount = float(self.amount_entry.get())
            if amount <= 0:
                raise ValueError("Сумма должна быть положительной.")
        except ValueError as ve:
            messagebox.showerror("Ошибка ввода", str(ve))
            return

        # Получение курсов валют и выполнение конвертации
        rates = fetch_exchange_rates(base_currency)
        if "error" in rates:
            messagebox.showerror("Ошибка", rates["error"])
            return

        result = convert_currency(amount, base_currency, target_currency, rates)
        if isinstance(result, str):
            messagebox.showerror("Ошибка", result)
        else:
            self.result_label.config(
                text=f"{amount:.2f} {base_currency} = {result:.2f} {target_currency}"
            )

    def run(self):
        """
        Запускает главный цикл приложения.
        """
        self.root.mainloop()

def run_gui():
    """
    Точка входа для запуска GUI-приложения.
    """
    app = CurrencyConverterUI()
    app.run()

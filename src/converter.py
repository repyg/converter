def convert_currency(amount, from_currency, to_currency, rates):
    """
    Конвертирует сумму из одной валюты в другую с использованием предоставленных курсов валют.
    
    :param amount: Сумма для конвертации.
    :param from_currency: Код исходной валюты.
    :param to_currency: Код целевой валюты.
    :param rates: Словарь с курсами валют.
    :return: Конвертированная сумма или сообщение об ошибке.
    """
    if "error" in rates:
        return rates["error"]
    
    if from_currency not in rates.get("rates", {}) or to_currency not in rates.get("rates", {}):
        return f"Валюта {from_currency} или {to_currency} недоступна в курсах валют."
    
    try:
        base_to_target_rate = rates["rates"][to_currency] / rates["rates"][from_currency]
        return amount * base_to_target_rate
    except Exception as e:
        return f"Ошибка при конвертации: {e}"

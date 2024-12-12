import requests
from requests.exceptions import HTTPError, ConnectionError, Timeout

API_URL = "https://api.exchangerate-api.com/v4/latest/"

def fetch_exchange_rates(base_currency="USD"):
    """
    Получает курсы валют из публичного API для заданной базовой валюты.
    
    :param base_currency: Базовая валюта для получения курсов (по умолчанию USD).
    :return: Словарь с курсами валют или сообщение об ошибке.
    """
    url = f"{API_URL}{base_currency}"
    for attempt in range(3):  # Логика повторов
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except HTTPError as http_err:
            return {"error": f"Произошла ошибка HTTP: {http_err}"}
        except ConnectionError:
            if attempt < 2:
                print("Ошибка подключения. Повторная попытка...")
            else:
                return {"error": "Не удалось подключиться после нескольких попыток."}
        except Timeout:
            return {"error": "Время запроса истекло."}
        except Exception as e:
            return {"error": str(e)}

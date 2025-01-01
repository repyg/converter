# Конвертер

Этот проект представляет собой утилиту на Python для конвертации данных из одного формата в другой.

## Установка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/repyg/converter.git
   ```

2. Перейдите в директорию проекта:

   ```bash
   cd converter
   ```

3. Создайте виртуальное окружение (рекомендуется):

   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Windows: venv\Scripts\activate
   ```

4. Установите необходимые зависимости:

   ```bash
   pip install -r requirements.txt
   ```

## Использование

Запустите основной скрипт с необходимыми аргументами:

```bash
python main.py --input input_file --output output_file
```

Где `input_file` — путь к входному файлу, а `output_file` — путь к выходному файлу.

## Требования

- Python 3.6 или выше
- Зависимости из `requirements.txt`


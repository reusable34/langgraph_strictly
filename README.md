# LangGraph Time Bot

A simple LangGraph-based chat bot that can tell you the current time.

## Setup

1. Создайте виртуальное окружение:
```bash
python -m venv .venv
```

2. Активируйте виртуальное окружение:
- Для Windows:
```bash
.venv\Scripts\activate
```
- Для Linux/Mac:
```bash
source .venv/bin/activate
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Создайте файл `.env` в корневой директории проекта и добавьте в него ваш API ключ:
```bash
OPENAI_API_KEY=your-api-key-here
```

## Run

1. Убедитесь, что вы находитесь в корневой директории проекта

2. Убедитесь, что файл `.env` существует и содержит правильный API ключ

3. Запустите приложение с поддержкой блокирующих операций:
```bash
langgraph dev --allow-blocking
```

## Test

Отправьте сообщение с вопросом о текущем времени, например: "What time is it?"

## Примечания

- Приложение запускается на http://127.0.0.1:2024
- Studio UI доступен по адресу: https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024
- API документация доступна по адресу: http://127.0.0.1:2024/docs
- Убедитесь, что файл `.env` добавлен в `.gitignore`, чтобы не публиковать API ключ в репозиторий
- Если возникают ошибки с блокирующими операциями, всегда используйте флаг `--allow-blocking` при запуске
- Перед запуском убедитесь, что нет других процессов, использующих порт 2024

## Устранение неполадок

Если возникают ошибки:

1. Удалите папку `.venv` и создайте новое виртуальное окружение:
```bash
rm -rf .venv
python -m venv .venv
```

2. Активируйте виртуальное окружение и переустановите зависимости:
```bash
.venv\Scripts\activate  # для Windows
pip install -r requirements.txt
```

3. Убедитесь, что файл `.env` существует и содержит правильный API ключ:
```bash
type .env  # для Windows
cat .env   # для Linux/Mac
```

4. Проверьте, что API ключ загружается:
```bash
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print('API Key:', os.getenv('OPENAI_API_KEY'))"
```

5. Запустите приложение снова:
```bash
langgraph dev --allow-blocking
```
  
FROM python:3.11

WORKDIR /app

# Устанавливаем Poetry
RUN pip install poetry

# Копируем файлы зависимостей
COPY poetry.lock pyproject.toml ./

# Устанавливаем зависимости
RUN poetry install

# Копируем остальные файлы
COPY . .

EXPOSE 8080

# Команда запуска
CMD ["poetry", "run", "uvicorn", "src.main:app", "--reload","--host", "0.0.0.0", "--port", "8080"]


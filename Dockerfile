# Какой язык программирования и версия
FROM python:latest
WORKDIR /SocialNetwork
# Копруем наш проект внутри папки(Docker)
COPY . /SocialNetwork
# Устанавливаем все библиотеки
RUN pip install -r requirements.txt
# Команда для запуска
CMD ["uvicorn", "main:app", "--reload", "--host=0.0.0.0", "--port-2525"]
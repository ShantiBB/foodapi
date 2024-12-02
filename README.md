# Тестовое задание - Django проект с PostgreSQL

Этот проект представляет собой тестовое задание, которое включает в себя Django модели для блюд и категорий блюд, а также предоставление API для получения списка категорий с опубликованными блюдами.

В проекте так же настроена админ зона.

## Развертывание проекта

Для работы с зависимостями используется Poetry. Для работы с базой данных PostgreSQL используется Docker.

### Склонируйте репозиторий:

```bash
git@github.com:ShantiBB/foodapi.git
cd foodapi
```

### Активация окружения:
```bash
python3 -m venv venv
source venv/bin/activate (для unix систем)
source venv/Scripts/activate (для windows систем)
```

### Устанавка и инициализация poetry:
```bash
pip install poetry
poetry init
poetry install
```

### Инициализация docker образа:
```bash
docker compose -f pg_docker/docker-compose-pg.yml up -d
```

### Запуск проекта и применение миграций:
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

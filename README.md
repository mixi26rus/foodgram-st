# Foodgram

## Описание проекта

Поект «Фудграм» — сайт, на котором пользователи будут публиковать свои рецепты, добавлять чужие рецепты в избранное и подписываться на публикации других авторов. Зарегистрированным пользователям также будет доступен сервис «Список покупок». Он позволит создавать список продуктов, которые нужно купить для приготовления выбранных блюд.

## Запуск проекта

Нужно клонировать репозиторий и перейти в него (директорию) в команддной строке:

```bash
git clone https://github.com/mixi26rus/foodgram-st.git 
```

```bash
cd foodgram-st
```

Необходимо запустить docker compose, находясь в нужных директориях:

```bash
cd infra
```
В директории `infra` необходимо создать файл `.env`, написать в нем следующее:

```
POSTGRES_USER=django
POSTGRES_PASSWORD=<your_password>
POSTGRES_DB=django
DB_HOST=db
DB_PORT=5432
SECRET_KEY=<your_secret_key>
ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0
DEBUG=False
```

```bash
docker compose up --build
```

Далее нужно выполнить миграции внутри БД:

```bash
docker compose exec backend python manage.py makemigrations users
```

```bash
docker compose exec backend python manage.py makemigrations recipes
```

```bash
docker compose exec backend python manage.py migrate
```

Следующим шагом нужно загрузить статику:

```bash
docker compose exec backend python manage.py collectstatic
```

И последний шаг – загрузить ингредиенты в БД :

```bash
docker compose exec backend python manage.py upload_bd
```

### Доступ к страницам по ссылкам:
`Главная страница` – `http://localhost:8000/`

`Админка` – `http://localhost:8000/admin/`

`Документация` – `http://localhost:8000//api/docs/`
